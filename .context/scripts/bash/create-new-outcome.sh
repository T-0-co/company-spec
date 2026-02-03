#!/usr/bin/env bash
# Create a new outcome directory with initial files

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/common.sh"

# Usage
usage() {
    cat <<EOF
Usage: $(basename "$0") [OPTIONS] <short-name>

Create a new knowledge outcome directory.

Arguments:
    short-name    2-4 word identifier (e.g., "authority-map", "product-glossary")

Options:
    --number NUM  Use specific number instead of auto-increment
    --json        Output result as JSON
    -h, --help    Show this help message

Examples:
    $(basename "$0") authority-map
    $(basename "$0") --number 005 product-glossary
EOF
}

# Parse arguments
JSON_OUTPUT=false
OUTCOME_NUMBER=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --json)
            JSON_OUTPUT=true
            shift
            ;;
        --number)
            OUTCOME_NUMBER="$2"
            shift 2
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        -*)
            echo "Unknown option: $1" >&2
            usage
            exit 1
            ;;
        *)
            break
            ;;
    esac
done

# Check for short name
if [[ $# -lt 1 ]]; then
    echo "Error: short-name is required" >&2
    usage
    exit 1
fi

SHORT_NAME="$1"

# Validate short name (lowercase, hyphens, no spaces)
if [[ ! "$SHORT_NAME" =~ ^[a-z][a-z0-9-]*$ ]]; then
    print_error "Invalid short name. Use lowercase letters, numbers, and hyphens only."
    exit 1
fi

# Find repository root
REPO_ROOT=$(find_repo_root) || {
    print_error "Not in a Company Context project"
    exit 1
}

# Check constitution exists
if ! has_constitution; then
    print_error "Constitution not found. Run /context.constitution first."
    exit 1
fi

# Get outcome number
if [[ -z "$OUTCOME_NUMBER" ]]; then
    OUTCOME_NUMBER=$(next_outcome_number)
fi

# Create outcome directory
OUTCOME_NAME="${OUTCOME_NUMBER}-${SHORT_NAME}"
OUTCOME_DIR="$REPO_ROOT/.context/outcomes/$OUTCOME_NAME"
TEMPLATES_DIR="$REPO_ROOT/.context/templates"

if [[ -d "$OUTCOME_DIR" ]]; then
    print_error "Outcome directory already exists: $OUTCOME_DIR"
    exit 1
fi

mkdir -p "$OUTCOME_DIR"
mkdir -p "$OUTCOME_DIR/checklists"

# Copy outcome template
if [[ -f "$TEMPLATES_DIR/outcome-template.md" ]]; then
    cp "$TEMPLATES_DIR/outcome-template.md" "$OUTCOME_DIR/outcome.md"

    # Replace placeholders
    sed -i "s/\[OUTCOME_NAME\]/${SHORT_NAME}/g" "$OUTCOME_DIR/outcome.md"
    sed -i "s/KO-\[###\]/KO-${OUTCOME_NUMBER}/g" "$OUTCOME_DIR/outcome.md"
    sed -i "s/\[###-outcome-name\]/${OUTCOME_NAME}/g" "$OUTCOME_DIR/outcome.md"
    sed -i "s/\[DATE\]/$(date +%Y-%m-%d)/g" "$OUTCOME_DIR/outcome.md"
fi

# Output result
if $JSON_OUTPUT; then
    cat <<EOF
{
    "outcome_id": "KO-$OUTCOME_NUMBER",
    "outcome_name": "$OUTCOME_NAME",
    "outcome_dir": "$OUTCOME_DIR",
    "files_created": ["outcome.md", "checklists/"]
}
EOF
else
    print_success "Created outcome: KO-$OUTCOME_NUMBER"
    echo "  Directory: $OUTCOME_DIR"
    echo "  Next: Edit outcome.md, then run /context.strategy"
fi
