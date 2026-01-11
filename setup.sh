#!/bin/bash
# Setup script for NeverEndingQuest

echo "=========================================="
echo "NeverEndingQuest - Setup"
echo "=========================================="
echo ""

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.9 or higher"
    exit 1
fi

echo "✓ Python found: $(python3 --version)"
echo ""

# Install requirements
echo "Installing Python packages..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✓ Packages installed successfully"
else
    echo "✗ Package installation failed"
    exit 1
fi

echo ""

# Setup config
if [ ! -f "config.py" ]; then
    echo "Setting up configuration..."
    cp config_template.py config.py
    echo "✓ Created config.py"
    echo ""
    echo "IMPORTANT: Edit config.py and add your OpenAI API key!"
    echo "Get one at: https://platform.openai.com/api-keys"
else
    echo "✓ config.py already exists"
fi

echo ""
echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Edit config.py and add your OpenAI API key"
echo "2. Run: python3 main.py"
echo ""
