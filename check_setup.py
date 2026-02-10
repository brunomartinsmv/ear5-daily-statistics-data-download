#!/usr/bin/env python3
"""
Utility script to check system readiness for ERA5 data downloads.
"""

import os
import sys
import shutil


def check_cdsapi_installation():
    """Check if cdsapi is installed."""
    try:
        import cdsapi
        print("✓ cdsapi is installed")
        return True
    except ImportError:
        print("✗ cdsapi is NOT installed")
        print("  Install with: pip install -r requirements.txt")
        return False


def check_credentials():
    """Check if CDS API credentials are configured."""
    cdsapirc_path = os.path.expanduser("~/.cdsapirc")
    if os.path.exists(cdsapirc_path):
        print(f"✓ Credentials file found at {cdsapirc_path}")
        # Read and validate format
        try:
            with open(cdsapirc_path, 'r') as f:
                content = f.read()
                if 'url:' in content and 'key:' in content:
                    print("  Credentials file appears valid")
                    return True
                else:
                    print("  ⚠ Credentials file may be incomplete")
                    print("  Should contain 'url:' and 'key:' lines")
                    return False
        except Exception as e:
            print(f"  ⚠ Error reading credentials file: {e}")
            return False
    else:
        print(f"✗ Credentials file NOT found at {cdsapirc_path}")
        print("  Create it with your CDS API credentials")
        print("  See .cdsapirc.example for format")
        return False


def check_disk_space(path='.', min_gb=10):
    """Check available disk space."""
    try:
        stat = shutil.disk_usage(path)
        free_gb = stat.free / (1024**3)
        print(f"✓ Disk space available: {free_gb:.2f} GB")
        if free_gb < min_gb:
            print(f"  ⚠ Warning: Less than {min_gb} GB available")
            print("    ERA5 files can be large. Consider freeing up space.")
            return False
        return True
    except Exception as e:
        print(f"✗ Could not check disk space: {e}")
        return False


def check_python_version():
    """Check Python version."""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 6:
        print(f"✓ Python version: {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"✗ Python version {version.major}.{version.minor} is too old")
        print("  Python 3.6+ is required")
        return False


def main():
    """Run all checks."""
    print("ERA5 Download System Readiness Check")
    print("=" * 50)
    print()
    
    checks = [
        ("Python version", check_python_version),
        ("cdsapi package", check_cdsapi_installation),
        ("API credentials", check_credentials),
        ("Disk space", check_disk_space),
    ]
    
    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append(result)
        except Exception as e:
            print(f"✗ Error checking {name}: {e}")
            results.append(False)
        print()
    
    print("=" * 50)
    if all(results):
        print("✓ All checks passed! You're ready to download ERA5 data.")
        print("\nNext steps:")
        print("  1. Review examples: python examples.py")
        print("  2. Or start downloading: python download_era5_daily.py --help")
        return 0
    else:
        print("✗ Some checks failed. Please address the issues above.")
        return 1


if __name__ == '__main__':
    sys.exit(main())
