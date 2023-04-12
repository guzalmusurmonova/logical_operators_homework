def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x1=a%10
    b=a%100
    x2=b//10
    x3=a//100
    return (x1+x2+x3)%2!=0
print(main(152))