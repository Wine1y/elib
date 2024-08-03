function getCookie(name){
    for (const cookie of document.cookie.split(";")) {
        const [cookieName, cookieValue] = cookie.split('=', 2)
        if (cookieName == name){
            return decodeURIComponent(cookieValue)
        }
    }
    return null
}