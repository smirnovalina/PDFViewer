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
        var percent = parseInt(data.correct_answer_count / data.question_count * 100);
        var mark = 2;
        if(percent > 80) mark = 5;
        else if(percent > 60) mark = 4;
        else if(percent > 40) mark = 3;
        alert('Result is ' + data.correct_answer_count  + '/' + data.question_count + ', your mark is ' + mark);
    }).catch(function(ex) {
        alert('parsing failed: ' + ex);
    });
}
