#!/bin/bash
# Batch Google OAuth Runner
# Runs multiple accounts sequentially with proper timeout and error handling

TIMEOUT=60  # seconds per account
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPT_PATH="$SCRIPT_DIR/google_oauth_stealth.py"
CONFIG_TEMPLATE="/tmp/oauth_config.env"
RESULTS_FILE="/tmp/oauth_batch_results.txt"

# Check if script exists
if [ ! -f "$SCRIPT_PATH" ]; then
    echo "Error: Script not found at $SCRIPT_PATH"
    exit 1
fi

# Clear results file
> "$RESULTS_FILE"

echo "============================================"
echo "Google OAuth Batch Runner"
echo "Timeout: ${TIMEOUT}s per account"
echo "============================================"
echo ""

# EXAMPLE ACCOUNTS - EDIT THIS ARRAY
# Format: "email:password"
ACCOUNTS=(
    "user1@example.com:password123"
    "user2@example.com:password456"
    "user3@example.com:password789"
)

# Alternatively, read from file:
# while IFS=: read -r email password; do
#     ACCOUNTS+=("$email:$password")
# done < accounts.txt

SUCCESS_COUNT=0
FAIL_COUNT=0
TOTAL=${#ACCOUNTS[@]}

for i in "${!ACCOUNTS[@]}"; do
    IFS=: read -r EMAIL PASSWORD <<< "${ACCOUNTS[$i]}"
    NUM=$((i + 1))
    
    echo "[${NUM}/${TOTAL}] Processing: ${EMAIL}"
    
    # Write config file
    cat > "$CONFIG_TEMPLATE" << EOF
EMAIL=$EMAIL
PASSWORD=$PASSWORD
PROVIDER=antigravity
OAUTH_URL=http://localhost:20128
EOF
    
    # Run script with timeout
    START=$(date +%s)
    OUTPUT=$(timeout $TIMEOUT python3 "$SCRIPT_PATH" 2>&1)
    EXIT_CODE=$?
    END=$(date +%s)
    ELAPSED=$((END - START))
    
    # Determine status
    if echo "$OUTPUT" | grep -q "CONNECTION SAVED"; then
        STATUS="✅ SUCCESS"
        ((SUCCESS_COUNT++))
    elif echo "$OUTPUT" | grep -q "GOOGLE REJECTED"; then
        STATUS="❌ REJECTED"
        ((FAIL_COUNT++))
    elif echo "$OUTPUT" | grep -q "BLOCKED"; then
        STATUS="🛡 BLOCKED"
        ((FAIL_COUNT++))
    elif [ $EXIT_CODE -eq 124 ]; then
        STATUS="⏰ TIMEOUT"
        ((FAIL_COUNT++))
    elif echo "$OUTPUT" | grep -q "No password field"; then
        STATUS="🔑 NO_PASS_FIELD"
        ((FAIL_COUNT++))
    elif echo "$OUTPUT" | grep -q "No email field"; then
        STATUS="📧 NO_EMAIL_FIELD"
        ((FAIL_COUNT++))
    else
        STATUS="❓ UNKNOWN"
        ((FAIL_COUNT++))
    fi
    
    echo "  → ${STATUS} (${ELAPSED}s)"
    echo "${EMAIL}|${STATUS}|${ELAPSED}s" >> "$RESULTS_FILE"
    
    # Brief pause between accounts
    if [ $NUM -lt $TOTAL ]; then
        sleep 2
    fi
done

# Summary
echo ""
echo "============================================"
echo "SUMMARY"
echo "============================================"
cat "$RESULTS_FILE"
echo ""
echo "Total: ${TOTAL} | Success: ${SUCCESS_COUNT} | Failed: ${FAIL_COUNT}"
echo "Results saved to: $RESULTS_FILE"
echo "============================================"

# Exit with appropriate code
if [ $SUCCESS_COUNT -gt 0 ] && [ $FAIL_COUNT -eq 0 ]; then
    exit 0
else
    exit 1
fi
