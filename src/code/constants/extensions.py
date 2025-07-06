# File extension to programming language mapping
FILE_EXTENSIONS = {
    # C/C++
    'cpp': 'cpp',
    'cc': 'cpp', 
    'cxx': 'cpp',
    'c': 'c',
    'h': 'c',
    
    # Go
    'go': 'go',
    
    # Java
    'java': 'java',
    
    # Kotlin
    'kt': 'kotlin',
    'kts': 'kotlin',
    
    # JavaScript
    'js': 'js',
    'jsx': 'js',
    
    # TypeScript
    'ts': 'ts',
    'tsx': 'ts',
    
    # PHP
    'php': 'php',
    
    # Protocol Buffers
    'proto': 'proto',
    
    # Python
    'py': 'python',
    'pyw': 'python',
    
    # reStructuredText
    'rst': 'rst',
    
    # Ruby
    'rb': 'ruby',
    
    # Rust
    'rs': 'rust',
    
    # Scala
    'scala': 'scala',
    'sc': 'scala',
    
    # Swift
    'swift': 'swift',
    
    # Markdown
    'md': 'markdown',
    'markdown': 'markdown',
    
    # LaTeX
    'tex': 'latex',
    'latex': 'latex',
    
    # HTML
    'html': 'html',
    'htm': 'html',
    
    # Solidity
    'sol': 'sol',
    
    # C#
    'cs': 'csharp',
    
    # COBOL
    'cob': 'cobol',
    'cbl': 'cobol',
    
    # Lua
    'lua': 'lua',
    
    # Perl
    'pl': 'perl',
    'pm': 'perl',
    
    # Haskell
    'hs': 'haskell',
    
    # Elixir
    'ex': 'elixir',
    'exs': 'elixir',
    
    # PowerShell
    'ps1': 'powershell'
}

def get_language_by_extension(extension: str) -> str | None:
    """Get programming language by file extension"""
    return FILE_EXTENSIONS.get(extension.lower())

def is_supported_extension(extension: str) -> bool:
    """Check if file extension is supported"""
    return extension.lower() in FILE_EXTENSIONS 
