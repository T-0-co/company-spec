#!/usr/bin/env bash
# Check prerequisites for Company Context Framework operations

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/common.sh"

# Parse arguments
JSON_OUTPUT=false
REQUIRE_CONSTITUTION=false
REQUIRE_OUTCOME=false
REQUIRE_STRATEGY=false
REQUIRE_TASKS=false
OUTCOME_DIR=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --json)
            JSON_OUTPUT=true
            shift
            ;;
        --require-constitution)
            REQUIRE_CONSTITUTION=true
            shift
            ;;
        --require-outcome)
            REQUIRE_OUTCOME=true
            shift
            ;;
        --require-strategy)
            REQUIRE_STRATEGY=true
            shift
            ;;
        --require-tasks)
            REQUIRE_TASKS=true
            shift
            ;;
        --outcome)
            OUTCOME_DIR="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1" >&2
            exit 1
            ;;
    esac
done

# Find repository root
REPO_ROOT=$(find_repo_root) || {
    if $JSON_OUTPUT; then
        echo '{"error": "Not in a Company Context project (no .context directory found)"}'
    else
        print_error "Not in a Company Context project (no .context directory found)"
    fi
    exit 1
}

CONTEXT_DIR="$REPO_ROOT/.context"
MEMORY_DIR="$CONTEXT_DIR/memory"
OUTCOMES_DIR="$CONTEXT_DIR/outcomes"
TEMPLATES_DIR="$CONTEXT_DIR/templates"

# Check results
ERRORS=()
WARNINGS=()
AVAILABLE_DOCS=()

# Check constitution
if [[ -f "$MEMORY_DIR/constitution.md" ]]; then
    AVAILABLE_DOCS+=("constitution.md")
else
    if $REQUIRE_CONSTITUTION; then
        ERRORS+=("Constitution not found. Run /context.constitution first.")
    else
        WARNINGS+=("No constitution found")
    fi
fi

# If outcome specified, check its documents
if [[ -n "$OUTCOME_DIR" ]]; then
    # Resolve full path if relative
    if [[ ! "$OUTCOME_DIR" = /* ]]; then
        OUTCOME_DIR="$OUTCOMES_DIR/$OUTCOME_DIR"
    fi

    if [[ -d "$OUTCOME_DIR" ]]; then
        if [[ -f "$OUTCOME_DIR/outcome.md" ]]; then
            AVAILABLE_DOCS+=("outcome.md")
        elif $REQUIRE_OUTCOME; then
            ERRORS+=("outcome.md not found in $OUTCOME_DIR")
        fi

        if [[ -f "$OUTCOME_DIR/strategy.md" ]]; then
            AVAILABLE_DOCS+=("strategy.md")
        elif $REQUIRE_STRATEGY; then
            ERRORS+=("strategy.md not found. Run /context.strategy first.")
        fi

        if [[ -f "$OUTCOME_DIR/tasks.md" ]]; then
            AVAILABLE_DOCS+=("tasks.md")
        elif $REQUIRE_TASKS; then
            ERRORS+=("tasks.md not found. Run /context.tasks first.")
        fi

        # Check for optional docs
        [[ -f "$OUTCOME_DIR/research.md" ]] && AVAILABLE_DOCS+=("research.md")
        [[ -d "$OUTCOME_DIR/checklists" ]] && AVAILABLE_DOCS+=("checklists/")
    else
        ERRORS+=("Outcome directory not found: $OUTCOME_DIR")
    fi
fi

# Output results
if $JSON_OUTPUT; then
    # Build JSON output
    cat <<EOF
{
    "repo_root": "$REPO_ROOT",
    "context_dir": "$CONTEXT_DIR",
    "outcome_dir": "$OUTCOME_DIR",
    "available_docs": $(printf '%s\n' "${AVAILABLE_DOCS[@]}" | jq -R . | jq -s .),
    "errors": $(printf '%s\n' "${ERRORS[@]}" 2>/dev/null | jq -R . | jq -s . || echo '[]'),
    "warnings": $(printf '%s\n' "${WARNINGS[@]}" 2>/dev/null | jq -R . | jq -s . || echo '[]'),
    "valid": $([ ${#ERRORS[@]} -eq 0 ] && echo true || echo false)
}
EOF
else
    echo "Company Context Framework - Prerequisites Check"
    echo "================================================"
    echo
    echo "Repository Root: $REPO_ROOT"
    echo "Context Dir: $CONTEXT_DIR"
    [[ -n "$OUTCOME_DIR" ]] && echo "Outcome Dir: $OUTCOME_DIR"
    echo

    echo "Available Documents:"
    for doc in "${AVAILABLE_DOCS[@]}"; do
        print_success "$doc"
    done
    echo

    if [[ ${#WARNINGS[@]} -gt 0 ]]; then
        echo "Warnings:"
        for warn in "${WARNINGS[@]}"; do
            print_warning "$warn"
        done
        echo
    fi

    if [[ ${#ERRORS[@]} -gt 0 ]]; then
        echo "Errors:"
        for err in "${ERRORS[@]}"; do
            print_error "$err"
        done
        exit 1
    fi

    print_success "All prerequisites met"
fi

# Exit with error if validation failed
[[ ${#ERRORS[@]} -eq 0 ]]
