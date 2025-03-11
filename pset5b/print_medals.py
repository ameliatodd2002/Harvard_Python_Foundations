def print_medals(medal_counts):
    g = "Gold"
    s = "Silver"
    b = "Bronze"
    t = "Total"
    print (f'{g:>23}  {s:>6}  {b:>6}  {t:>6}')
    for x in medal_counts:
        print (f'{x:>15}  {medal_counts[x][0]:>6}  {medal_counts[x][1]:>6}  {medal_counts[x][2]:>6}  {(medal_counts[x][0] + medal_counts[x][1] + medal_counts[x][2]):>6}')


def main():
    MEDAL_COUNTS = {
        "Canada" : [ 0, 3, 0 ],
        "Italy" : [ 0, 0, 1 ],
        "Germany" : [ 0, 0, 1 ],
        "Japan" : [ 1, 0, 0 ],
        "Kazakhstan" : [ 0, 0, 1 ],
        "Russia" : [ 3, 1, 1 ],
        "South Korea" : [ 0, 1, 0 ],
        "United States" : [ 1, 0, 1 ]
        }
    print_medals(MEDAL_COUNTS)


if __name__ == "__main__":
    main()


