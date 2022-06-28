class ParkingSystem {
public:
    ParkingSystem(int big, int medium, int small) {
        mpp[1] = big;
        mpp[2] = medium;
        mpp[3] = small;
    }
    
    bool addCar(int carType) {
        if(mpp[carType] > 0){
            mpp[carType]--;
            return true;
        }
        return false;
    }
private:
    unordered_map<int,int> mpp;
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */