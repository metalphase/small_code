import math

class Solution:

    def track_time(self, dist, velocity):
        '''returns the time to travel dist at velocity velocity
        '''

        t = 0.0

        for track in dist:

            # We advance to the top of the hour at the end of every train
                # ride
                t = math.ceil(t)

                # We add the time of each train to current_time
                t += track/velocity
        
        return t


    def minSpeedOnTime(self, dist, hour):
        

        # No matter what speed, the trains run at the top of each hour,
        # meaning that it takes at minimum len(dist) to complete the 
        # commute by train. If this is already larger than the hour
        # commitment, we return -1 since it is unfeasible
        if len(dist) - 1 >= hour:
            return -1

        # We will use a binary search to find the minimal velocity that will
        # make us on time to work. We set our high and low values respectively
        low_vel = 1
        high_vel = 10**7

        # We run a while loop while our bounds don't pass each other
        while low_vel < high_vel:

            # define a midway point and evaluate whether it is on time or late
            mid_vel = low_vel + (high_vel - low_vel)//2
            # If our midway velocity is already fast enough, we set it to be 
            # our new high bound and search for the minimal velocity below it.
            # Otherwise, we set a new boundary for our lower bound
            if self.track_time(dist, mid_vel) <= hour:

                print(self.track_time(dist, mid_vel))
                high_vel = mid_vel
            else:
                low_vel = mid_vel + 1

            
        return high_vel



sol = Solution()
print(sol.minSpeedOnTime([1,3,2], 6))
print('__________________________')
print(sol.minSpeedOnTime([1,3,2], 2.7))
print('__________________________')
print(sol.minSpeedOnTime([1,3,2], 1.9))

