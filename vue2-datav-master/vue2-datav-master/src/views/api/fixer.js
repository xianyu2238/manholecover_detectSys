import service from "./axios";


export function getMap(data){
    return service({
        url:"/v1/getMap",
        method:"post",
        data:data
    })
}
export function getPoints(data){
    return service({
        url:"/v1/getPoints",
        method:"post",
        data:data
    })
}
export function detect(data){
    return service({
        url:"/v2/detect",
        method:"post",
        data:data
    })
}
export function getFixTask(data){
    return service({
        url:"/v1/getFixTask",
        method:"post",
        data:data
    })
}

export function uploadImage(data){
    return service({
        url:"/v1/uploadImage",
        method:"post",
        data:data
    })
}

export function submitPoint(data){
    return service({
        url:"/v1/submitPoint",
        method:"post",
        data:data
    })
}

export function submitTask(data){
    return service({
        url:"/v1/submitTask",
        method:"post",
        data:data
    })
}
