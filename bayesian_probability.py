"""
source: below problem statement is taken from hackerearth

Bob has an important meeting tomorrow and he has to reach office on time in morning. His general mode of transport is by car and on a regular day (no car trouble) the probability that he will reach on time is pot. The probability that he might have car trouble is pct. If the car runs into trouble he will have to take a train and only 2 trains out of the available N trains will get him to office on time.
What are the chances that he will reach office on time tomorrow?
"""


def basian_probability():
    pct = float(input())
    pot = float(input())
    N = int(input())

    prob = (1-pct)*pot + pct*2/N

    print("%.6f" % prob)


if __name__ == "__main__":
    basian_probability()
