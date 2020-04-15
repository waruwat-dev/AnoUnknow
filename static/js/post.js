
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
function postCreate(e, url) {
    var text = e.getElementsByClassName("text")
    // var url = "{% url 'create_post' %}"
    fetch(url, {
        method: 'POST',
        body: {
            text
        }
    })
        // .then(res => console.log(res))
        .catch(err => alert(err))
    console.log(url)

}


function socketOnMessage(e) {
    var data = JSON.parse(e.data).message;
    // console.log(data)

    if (data.comment) {
        var element = document.getElementById("comment_" + data.comment)
    } else {
        var element = document.getElementById("post_" + data.post)
    }
    console.log(element)
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
