class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        if original ==  color :
            return image
        row, col = len(image), len(image[0])
        #neighbor 
        neighbor = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def fill(dr, dc) : 
            #On s'arrete si la case est hors grille ou n'a pas la couleur d'origine
            if not ((0 <= dr < row) and (0 <= dc < col)) or image[dr][dc] != original:
                return
            image[dr][dc] = color
            for r, c in neighbor : 
                fill(dr+r, dc+c)
        fill(sr, sc)   
        return image
            