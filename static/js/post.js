
var baseUrl = window.location.protocol + "//" + window.location.host
async function emotion_post(post, type, element) {
    fetch(baseUrl + `/post/emotion/${post}/${type}`, {
        method: 'POST'
    })
        // .then(res => console.log(res))
        .catch(err => alert(err))
}

async function emotion_comment(comment, type, element) {
    fetch(baseUrl + `/comment/emotion/${comment}/${type}`, {
        method: 'POST'
    })
        // .then(res => console.log(res))
        .catch(err => alert(err))
}


// function distribute() {
//     const data = { numberOfDistribution: 1 };

//     var url = 'http://127.0.0.1:8000/post/api/post/';
//     var data = { numberOfDistribution: 1 };
//     fetch(url, {
//         method: 'POST', // or 'PUT'
//         body: JSON.stringify(data), // data can be `string` or {object}!
//         headers: {
//             'Content-Type': 'application/json'
//         }
//     }).then(res => res.json())
//         .then(response => console.log('Success:', JSON.stringify(response)))
//         .catch(error => console.error('Error:', error));
// }
// function postCreate(e, url) {
//     var text = e.getElementsByClassName("text")
//     // var url = "{% url 'create_post' %}"
//     fetch(url, {
//         method: 'POST',
//         body: {
//             text
//         }
//     })
//         // .then(res => console.log(res))
//         .catch(err => alert(err))
//     console.log(url)

// }

function commentCreate(post_id, url) {
    var comment = document.getElementById("comment_post" + post_id)
    var text = comment.value
    comment.value = ""
    const formData = new FormData();
    formData.append('text', text);
    fetch(url, {
        method: 'POST',
        body: formData
    })
        // .then(res => console.log(res))
        .catch(err => alert(err))
}

function getComment(comment_id) {
    fetch('/comment/getcomment/' + comment_id)
        .then(res => res.json())
        .then(data => insertComment(data))
        .catch(err => alert(err))

}

function insertComment(comment) {
    var div = document.createElement('div');
    var post = document.getElementById("post_" + comment.post_id)
    var commentArea = post.getElementsByClassName('comment_area')[0]
    var html = `
    <div class="card m-1" id="comment_${comment.id}">
        <div class="card-body">
            <h6>${comment.text}</h6>
            <div class="btn-group mr-2" role="group" aria-label="First group">
                <button type="submit" class="btn btn-secondary"
                    onclick="emotion_comment(${comment.id}, 1, this)">👍<span
                        class="like">${comment.like}</span></button>
                <button type="submit" class="btn btn-secondary"
                    onclick="emotion_comment(${comment.id}, 2, this)">😂<span
                        class="haha">${comment.haha}</span></button>
                <button type="submit" class="btn btn-secondary"
                    onclick="emotion_comment(${comment.id}, 3, this)">😠<span
                        class="angry">${comment.angry}</span></button>
                <button type="submit" class="btn btn-secondary"
                    onclick="emotion_comment(${comment.id}, 4, this)">😭<span
                        class="sad">${comment.sad}</span></button>
            </div>
        </div>
    </div>`
    div.innerHTML = html
    commentArea.appendChild(div)
}


function socketOnMessage(e) {
    var data = JSON.parse(e.data).message;
    // console.log(data)
    if (data.addComment) {
        getComment(data.addComment)
        return
    }
    if (data.comment) {
        var element = document.getElementById("comment_" + data.comment)
    } else {
        var element = document.getElementById("post_" + data.post)
    }
    if (data.like) {
        var like = element.getElementsByClassName("like")[0]
        like.innerText = data.like
    }
    else if (data.haha) {
        var haha = element.getElementsByClassName("haha")[0]
        haha.innerText = data.haha
    }
    else if (data.angry) {
        var angry = element.getElementsByClassName("angry")[0]
        angry.innerText = data.angry
    }
    else if (data.sad) {
        var sad = element.getElementsByClassName("sad")[0]
        sad.innerText = data.sad
    }

};
