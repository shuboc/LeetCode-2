// Time:  O(n)
// Space: O(k)

class ZigzagIterator {
public:
    ZigzagIterator(vector<int>& v1, vector<int>& v2) {
        if (!v1.empty()) {
            q.emplace(v1.size(), v1.cbegin());
        }
        if (!v2.empty()) {
            q.emplace(v2.size(), v2.cbegin());
        }
    }

    int next() {
        const auto len = q.front().first;
        const auto it = q.front().second;
        q.pop();
        if (len > 1) {
            q.emplace(len - 1, it + 1);
        }
        return *it;
    }

    bool hasNext() {
        return !q.empty();
    }

private:
    queue<pair<int, vector<int>::const_iterator>> q;
};

/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * ZigzagIterator i(v1, v2);
 * while (i.hasNext()) cout << i.next();
 */
