import sys 

mx = 0
seats = []

def get_range( x, y, i):
   c = seat[i]

   if i == 9 and c == 'L':
      return x
   if i == 9 and c == 'R':
      return y
   if i == 6 and c == 'F':
      return x
   if i == 6 and c == 'B':
      return y
   if c == 'L' or c == 'F':
      return int(get_range(x,int((x+y)/2),i+1))
   if c == 'R' or c == 'B':
      return int(get_range(int((x+y+1)/2),y,i+1))


for line in sys.stdin:
    seat = line.strip()
    row = get_range(0,127,0)
    col = get_range(0,7,7)
    seat_id = row * 8 + col
    seats.append(seat_id)

#print(sorted(seats))

for seat in range(1023):
   if (seat not in seats) and (seat+1 in seats) and (seat-1 in seats):
       print(seat)
