import service from "./axios";


export function userLog(data){
    return service({
        url:"/v1/userLog",
        method:"post",
        data:data
    })
}

export function getArea(data){
    return service({
        url:"/v1/getArea",
        method:"post",
        data:data
    })
}