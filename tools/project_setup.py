# File: esp32s3-api-framework/tools/project_setup.py

import os
import shutil
import argparse

def create_directory(path):
    """
    Create a directory if it doesn't exist.
    
    Args:
        path (str): The directory path to create.
    
    Raises:
        OSError: If directory creation fails.
    """
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as e:
        print(f"Error creating directory {path}: {e}")
        raise

def create_file(path, content=""):
    """
    Create a file with optional content.
    
    Args:
        path (str): The file path to create.
        content (str): Optional content to write to the file.
    
    Raises:
        IOError: If file creation or writing fails.
    """
    try:
        with open(path, 'w') as f:
            f.write(content)
    except IOError as e:
        print(f"Error creating file {path}: {e}")
        raise

def setup_project(base_path):
    """
    Set up the project directory structure and create necessary files.
    
    Args:
        base_path (str): The base path for the project.
    
    Raises:
        Exception: If any step in the setup process fails.
    """
    try:
        # Create main directories
        directories = [
            'src/core', 'src/services', 'src/plugins', 'src/communication', 'src/ml',
            'include', 'lib', 'test', 'tools', 'docs', 'examples'
        ]
        for directory in directories:
            create_directory(os.path.join(base_path, directory))

        # Create essential files
        create_file(os.path.join(base_path, 'CMakeLists.txt'), "cmake_minimum_required(VERSION 3.5)\ninclude($ENV{IDF_PATH}/tools/cmake/project.cmake)\nproject(esp32s3-api-framework)")
        create_file(os.path.join(base_path, 'sdkconfig'))
        create_file(os.path.join(base_path, 'README.md'), "# ESP32-S3 API Framework\n\nThis project is an API service framework for the ESP32-S3.")
        create_file(os.path.join(base_path, '.gitignore'), "build/\nsdkconfig.old\n")

        # Copy this setup script to the tools directory
        shutil.copy(__file__, os.path.join(base_path, 'tools', 'project_setup.py'))

        print(f"Project structure created successfully at {base_path}")
    except Exception as e:
        print(f"Error setting up project: {e}")
        raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Set up ESP32-S3 API Framework project structure")
    parser.add_argument("path", help="Base path for the project")
    args = parser.parse_args()

    setup_project(args.path)
