function takeBook(bookID){
    return fetch("/api/books/take", {
        method: "POST",
        body: JSON.stringify({id: bookID}),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
}

function returnBook(bookID){
    return fetch("/api/books/return", {
        method: "POST",
        body: JSON.stringify({id: bookID}),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
}