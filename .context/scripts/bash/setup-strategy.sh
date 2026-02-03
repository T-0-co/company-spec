#!/usr/bin/env bash
# Set up strategy file for an outcome

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/common.sh"

# Usage
usage() {
    cat <<EOF
Usage: $(basename "$0") [OPTIONS] <outcome-dir>

Set up strategy file for a knowledge outcome.

Arguments:
    outcome-dir   Outcome directory name or path (e.g., "001-authority-map")

Options:
    --json        Output result as JSON
    -h, --help    Show this help message

Examples:
    $(basename "$0") 001-authority-map
    $(basename "$0") .context/outcomes/001-authority-map
EOF
}

# Parse arguments
JSON_OUTPUT=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --json)
            JSON_OUTPUT=true
            shift
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

# Check for outcome dir
if [[ $# -lt 1 ]]; then
    echo "Error: outcome-dir is required" >&2
    usage
    exit 1
fi

OUTCOME_INPUT="$1"

# Find repository root
REPO_ROOT=$(find_repo_root) || {
    print_error "Not in a Company Context project"
    exit 1
}

OUTCOMES_DIR="$REPO_ROOT/.context/outcomes"
TEMPLATES_DIR="$REPO_ROOT/.context/templates"

# Resolve outcome directory
if [[ "$OUTCOME_INPUT" = /* ]]; then
    OUTCOME_DIR="$OUTCOME_INPUT"
elif [[ -d "$OUTCOMES_DIR/$OUTCOME_INPUT" ]]; then
    OUTCOME_DIR="$OUTCOMES_DIR/$OUTCOME_INPUT"
elif [[ -d "$OUTCOME_INPUT" ]]; then
    OUTCOME_DIR="$(cd "$OUTCOME_INPUT" && pwd)"
else
    print_error "Outcome directory not found: $OUTCOME_INPUT"
    exit 1
fi

# Check outcome.md exists
if [[ ! -f "$OUTCOME_DIR/outcome.md" ]]; then
    print_error "outcome.md not found in $OUTCOME_DIR"
    print_error "Run /context.outcome first"
    exit 1
fi

# Check strategy doesn't already exist
if [[ -f "$OUTCOME_DIR/strategy.md" ]]; then
    print_warning "strategy.md already exists in $OUTCOME_DIR"
    if ! $JSON_OUTPUT; then
        read -p "Overwrite? [y/N] " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            exit 0
        fi
    fi
fi

# Extract outcome name from directory
OUTCOME_NAME=$(basename "$OUTCOME_DIR")
OUTCOME_NUMBER=${OUTCOME_NAME%%-*}

# Copy strategy template
if [[ -f "$TEMPLATES_DIR/strategy-template.md" ]]; then
    cp "$TEMPLATES_DIR/strategy-template.md" "$OUTCOME_DIR/strategy.md"

    # Replace placeholders
    sed -i "s/\[OUTCOME_NAME\]/${OUTCOME_NAME#*-}/g" "$OUTCOME_DIR/strategy.md"
    sed -i "s/KO-\[###\]/KO-${OUTCOME_NUMBER}/g" "$OUTCOME_DIR/strategy.md"
    sed -i "s/\[###-outcome-name\]/${OUTCOME_NAME}/g" "$OUTCOME_DIR/strategy.md"
    sed -i "s/\[DATE\]/$(date +%Y-%m-%d)/g" "$OUTCOME_DIR/strategy.md"
fi

# Output result
if $JSON_OUTPUT; then
    cat <<EOF
{
    "outcome_dir": "$OUTCOME_DIR",
    "strategy_file": "$OUTCOME_DIR/strategy.md",
    "outcome_file": "$OUTCOME_DIR/outcome.md"
}
EOF
else
    print_success "Created strategy.md for $OUTCOME_NAME"
    echo "  File: $OUTCOME_DIR/strategy.md"
    echo "  Next: Edit strategy.md, then run /context.tasks"
fi
