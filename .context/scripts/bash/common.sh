#!/usr/bin/env bash
# Common functions for Company Context Framework scripts

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Find repository root (looks for .context directory)
find_repo_root() {
    local dir="$PWD"
    while [[ "$dir" != "/" ]]; do
        if [[ -d "$dir/.context" ]]; then
            echo "$dir"
            return 0
        fi
        dir="$(dirname "$dir")"
    done
    return 1
}

# Print colored message
print_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

# Check if constitution exists
has_constitution() {
    local root
    root=$(find_repo_root) || return 1
    [[ -f "$root/.context/memory/constitution.md" ]]
}

# Get list of outcomes
list_outcomes() {
    local root
    root=$(find_repo_root) || return 1
    local outcomes_dir="$root/.context/outcomes"

    if [[ -d "$outcomes_dir" ]]; then
        find "$outcomes_dir" -maxdepth 1 -type d -name '[0-9]*' | sort
    fi
}

# Get next outcome number
next_outcome_number() {
    local root
    root=$(find_repo_root) || return 1
    local outcomes_dir="$root/.context/outcomes"
    local max=0

    if [[ -d "$outcomes_dir" ]]; then
        for dir in "$outcomes_dir"/[0-9]*; do
            if [[ -d "$dir" ]]; then
                local name=$(basename "$dir")
                local num=${name%%-*}
                num=$((10#$num))  # Force decimal interpretation
                if (( num > max )); then
                    max=$num
                fi
            fi
        done
    fi

    printf "%03d" $((max + 1))
}

# Check if file has unresolved clarifications
has_clarifications() {
    local file="$1"
    grep -q '\[NEEDS CLARIFICATION\]' "$file" 2>/dev/null
}

# Count tasks in a tasks.md file
count_tasks() {
    local file="$1"
    local total=0
    local complete=0

    if [[ -f "$file" ]]; then
        total=$(grep -c '^\- \[[ xX]\] T[0-9]' "$file" 2>/dev/null || echo 0)
        complete=$(grep -c '^\- \[[xX]\] T[0-9]' "$file" 2>/dev/null || echo 0)
    fi

    echo "$complete/$total"
}

# Get outcome status
outcome_status() {
    local outcome_dir="$1"

    if [[ ! -f "$outcome_dir/outcome.md" ]]; then
        echo "missing-outcome"
        return
    fi

    if [[ ! -f "$outcome_dir/strategy.md" ]]; then
        echo "needs-strategy"
        return
    fi

    if [[ ! -f "$outcome_dir/tasks.md" ]]; then
        echo "needs-tasks"
        return
    fi

    local progress=$(count_tasks "$outcome_dir/tasks.md")
    local complete=${progress%/*}
    local total=${progress#*/}

    if [[ "$complete" == "$total" ]] && [[ "$total" -gt 0 ]]; then
        echo "complete"
    else
        echo "in-progress ($progress)"
    fi
}

# Export functions for use in other scripts
export -f find_repo_root print_info print_success print_warning print_error
export -f has_constitution list_outcomes next_outcome_number
export -f has_clarifications count_tasks outcome_status
