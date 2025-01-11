class MyQueue {
public:
    // push element x to the back of the queue
    void push(int x) {
       while(!input.empty()) {
           output.push(input.top());
           input.pop();
       }
       input.push(x);
       while (!output.empty()) {
           input.push(output.top());
           output.pop();
       }
    }
    // remove the element from the front and return in
    int pop() {
       if (!input.empty()) {
           int val = input.top();
           input.pop();
           return val;
       }
       return -1;
    }
    // return the element from the front
    int peek() {
        if (!input.empty())
            return input.top();
        return -1;
    }
    
    bool empty() {
        return input.size() == 0;
    }
private:
    stack<int> input;
    stack<int> output;
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
