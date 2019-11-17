def last_letter(word):
    result=word[-1]
    return result


#write your code here...
#DO NOT remove lines below here, this is designed to test your code.
def test_last_letter():
    assert last_letter('hello!') == '!'
    assert last_letter('banana') == 'a'
    assert last_letter('8') == '8'
    assert last_letter('funnyguys') == 's'
    assert last_letter('101') == '1'
    print("YOUR CODE IS CORRECT!")

test_last_letter()
