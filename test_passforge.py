import subprocess
import sys
import os


def run_command(cmd):
    """Run shell command and return output."""
    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True,
        cwd=os.path.dirname(os.path.abspath(__file__)),
    )
    return result.stdout.strip(), result.stderr.strip(), result.returncode


def test_basic_generation():
    """Test basic password generation."""
    stdout, stderr, code = run_command("python passforge.py")
    assert code == 0
    assert len(stdout) == 16
    assert any(c.isupper() for c in stdout)
    assert any(c.islower() for c in stdout)
    assert any(c.isdigit() for c in stdout)
    assert any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?" for c in stdout)


def test_custom_length():
    """Test custom password length."""
    stdout, stderr, code = run_command('python passforge.py -l 20')
    assert code == 0
    assert len(stdout) == 20


def test_no_symbols():
    """Test password without symbols."""
    stdout, stderr, code = run_command("python passforge.py --no-symbols -l 16")
    assert code == 0
    assert len(stdout) == 16
    assert not any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?" for c in stdout)


def test_batch_generation():
    """Test batch generation."""
    stdout, stderr, code = run_command("python passforge.py -c 5 -l 10")
    assert code == 0
    lines = stdout.split('\n')
    assert len(lines) == 5
    for line in lines:
        if line.startswith('.'):
            password = line.split('. ')[1] if '. ' in line else line
            if password:
                assert len(password) == 10


def test_exclude_chars():
    """Test character exclusion."""
    stdout, stderr, code = run_command('python passforge.py --exclude "O0" -l 20')
    assert code == 0
    assert len(stdout) == 20
    assert 'O' not in stdout
    assert '0' not in stdout


def test_help():
    """Test help option."""
    stdout, stderr, code = run_command("python passforge.py --help")
    assert code == 0
    assert "usage:" in stdout.lower()


if __name__ == "__main__":
    tests = [
        ("Basic generation", test_basic_generation),
        ("Custom length", test_custom_length),
        ("No symbols", test_no_symbols),
        ("Batch generation", test_batch_generation),
        ("Exclude characters", test_exclude_chars),
        ("Help option", test_help),
    ]

    for name, test_func in tests:
        try:
            test_func()
            print(f"[PASS] {name}")
        except Exception as e:
            print(f"[FAIL] {name} - {e}")
            sys.exit(1)

    print("\nAll tests passed!")
