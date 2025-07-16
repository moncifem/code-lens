# CodeLens

**Knowledge for all, straight from your repo.**

CodeLens turns any Git repository into a searchable knowledge base. It automatically clones a repo, chunks the code, and uses vector embeddings to make the contents easily searchable.

## Getting Started

### Requirements
*   Python >= 3.11
*   [UV](https://github.com/astral-sh/uv)

### Installation & Usage
1.  **Clone & Install:**
    ```bash
    git clone https://github.com/moncifem/code-lens.git
    cd code-lens/src
    uv sync
    ```

2.  **Run:**
    ```bash
    python main.py
    ```

## License
This project is licensed under the [MIT License](LICENSE).
