class Solution:
    def countTriplets(self, arr, target):
        n = len(arr)
        count = 0

        # i ko fix karte hain, aur left & right pointers se check karte hain
        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                # triplet ka sum nikalte hain
                total = arr[i] + arr[left] + arr[right]

                if total == target:
                    # agar left aur right dono same element par hain
                    if arr[left] == arr[right]:
                        # total elements between left and right
                        length = right - left + 1
                        # total combinations = nC2 = (n*(n-1))/2
                        count += (length * (length - 1)) // 2
                        break  # sab combinations count ho gaye, toh break karte hain

                    else:
                        # left wale element ka count nikalte hain
                        l_count = 1
                        while left + 1 < right and arr[left] == arr[left + 1]:
                            l_count += 1
                            left += 1

                        # right wale element ka count nikalte hain
                        r_count = 1
                        while right - 1 > left and arr[right] == arr[right - 1]:
                            r_count += 1
                            right -= 1

                        # total combinations = left_count * right_count
                        count += l_count * r_count

                        # next unique elements pe move karte hain
                        left += 1
                        right -= 1

                elif total < target:
                    # agar sum chhota hai target se, toh left ko aage badhao
                    left += 1
                else:
                    # agar sum bada hai target se, toh right ko piche le jao
                    right -= 1

        return count
