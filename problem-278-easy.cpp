// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int left = 1;
        int right = n;
        int first = n;
        int mid = 0;
        while (left <= right) {
            mid = left + (right - left) / 2; // prevent overflow
            int bad = isBadVersion(mid);
            if (bad && !isBadVersion(mid-1))
                break;
            else if (!bad)
                left = mid + 1;
            else
                right = mid - 1;
        }
        return mid;
    }
};
