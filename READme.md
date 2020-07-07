## What is -One Time Pad Cipher-?

* The term "one-time pad" refers to any method of encryption where each byte of the plaintext is encrypted using one byte of the key stream and each key byte is used one time then never used again.

* [More about](https://scialert.net/fulltext/?doi=itj.2005.87.95)

* This is an implemention of OTP in Python

### Problems to fix
- [ ] If the user inputs an unequal length of the pad and message, it throws an error
- [x] whitespace_positions and capitalized_positions can have same indexes in them because of the trimming
  * Comment: Indexes are fixed, but when adding back spaces and capitals, **first add spaces, then capitals**
