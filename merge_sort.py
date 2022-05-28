def mergeSort(similarity):
    if len(similarity) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(similarity)//2
        L = similarity[:r]
        M = similarity[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                similarity[k] = L[i]
                i += 1
            else:
                similarity[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            similarity[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            similarity[k] = M[j]
            j += 1
            k += 1
