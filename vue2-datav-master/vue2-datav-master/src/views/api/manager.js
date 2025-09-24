import service from "./axios";


export function getErrorArea(){
    return service({
        url:"/v1/getErrorArea",
        method:"get",
    })
}

export function getAllTask(){
    return service({
        url:"/v1/getAllTask",
        method:"get",
    })
}


export function getAllfixer(){
    return service({
        url:"/v1/getAllFixer",
        method:"get",
    })
}

export function registerPerson(data){
    return service({
        url:"/v1/registerPerson",
        method:"post",
        data:data
    })
}

export function publishTask(data){
    return service({
        url:"/v1/publishTask",
        method:"post",
        data:data
    })
}

export function getTaskProgress(data){
    return service({
        url:"/v1/getTaskProgress",
        method:"post",
        data:data
    })
}

export function checkTask(data){
    return service({
        url:"/v1/checkTask",
        method:"post",
        data:data
    })
}
