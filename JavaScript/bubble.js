
// swapped = true
function bubble(arr){
    var swapped = true;
    while(swapped){
        swapped = false;
        for(var i = 0;i < arr.length; i++){
            if (arr[i] > arr[i+1]){
                var temp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = temp;
                swapped = true;
            }
        }
    }
    console.log(arr);
}
    // swapped = true
    // i = 0
    // while swapped == true:
    //     while i < len(arr):
    //         print arr[i]
    //         swapped = true
    //         i += 1
    //     swapped = false

bubble([5,3,1,0,6,3,4,9,1,3,5,2,7,-1,6,10,0,0,5])
