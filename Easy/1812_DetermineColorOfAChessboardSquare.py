class Solution(object):
    def squareIsWhite(self, coordinates):
        b= int(coordinates[1])
        x= coordinates[0]
        if( ((b%2 ==1) and (x in 'aceg')) or ((b%2==0) and (x not in 'aceg'))):
            return False
        return True
