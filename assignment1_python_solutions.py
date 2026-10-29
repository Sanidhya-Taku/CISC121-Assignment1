# CISC 121 Assignment 1 - reference solutions
# AI assistance: OpenAI ChatGPT (GPT-6), October 27, 2026.
# Each Codility task uses a function named solution; copy one at a time.

# --- CyclicRotation ---
def solution(A, K):
    if not A:
        return A
    shift = K % len(A)
    return A[-shift:] + A[:-shift] if shift else A[:]

# --- OddOccurrencesInArray ---
def solution(A):
    unmatched = 0
    for value in A:
        unmatched ^= value
    return unmatched

# --- FrogJmp ---
def solution(X, Y, D):
    distance = Y - X
    return (distance + D - 1) // D

# --- PermMissingElem ---
def solution(A):
    n = len(A) + 1
    expected = n * (n + 1) // 2
    return expected - sum(A)

# --- TapeEquilibrium ---
def solution(A):
    right = sum(A)
    left = 0
    best = float('inf')
    for value in A[:-1]:
        left += value
        right -= value
        best = min(best, abs(left - right))
    return best

