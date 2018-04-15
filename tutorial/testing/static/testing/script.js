function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function postResult(questionCount) {
    var correctAnswerCount = 0;
    var checked_answers = document.querySelectorAll('input:checked');
    if(questionCount !== checked_answers.length){
        alert('Please answer all questions!');
        return false;
    }
    [].forEach.call(checked_answers, function(el){
        if(el.value === el.dataset.correct){
            correctAnswerCount++;
        }
    });
    var data = {
        question_count: questionCount,
        correct_answer_count: correctAnswerCount
    };
    fetch('/result/', {
        method: 'post',
        credentials: 'same-origin',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }).then(function(response) {
        return response.json();
    }).then(function(data) {
        alert('Result is ' + parseInt(data.correct_answer_count / data.question_count * 100) + '%');
    }).catch(function(ex) {
        alert('parsing failed: ' + ex);
    });
}
