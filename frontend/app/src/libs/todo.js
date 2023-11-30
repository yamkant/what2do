function getTimeNow() {
    const now = new Date();
    function padZero(value) {
        return value < 10 ? `0${value}` : value;
    }
    const formattedDateTime = `${now.getFullYear()}-${padZero(now.getMonth() + 1)}-${padZero(now.getDate())} ${padZero(now.getHours())}:${padZero(now.getMinutes())}`;
    return formattedDateTime.substring(formattedDateTime.length - 5)
}

function cvtStringToDate(timeStr) {
    const currentDate = new Date();
    const [hours, minutes] = timeStr.split(':');
    const timeDate = new Date(currentDate.getFullYear(), currentDate.getMonth(), currentDate.getDate(), hours, minutes);
    return timeDate;
}

function getTimeParts(timeString) {
    if (!timeString) {
        return null
    }
    const date = new Date(timeString);
    const h = date.getHours();
    const m = date.getMinutes();
    const s = date.getSeconds();
    return new Date(0, 0, 0, h, m, s);
}

function cvtIsoStringToTime(timeString) {
    if (!timeString) {
        return "";
    }
    const date = new Date(timeString);
    const h = String(date.getHours()).padStart(2, '0');
    const m = String(date.getMinutes()).padStart(2, '0');
    const s = String(date.getSeconds()).padStart(2, '0');
    return `${h}:${m}:${s}`;
}

function isTimeFormat(timeString) {
    let offsetPattern = /([+-]\d{2}):(\d{2})$/;
    if (offsetPattern.test(timeString)) {
         return true;
    }
    offsetPattern = /Z$/;
    if (offsetPattern.test(timeString)) {
         return true;
    }
    return false;
}

function cvtTodoToRequestData(todo) {
    const retData = {}
    for (let key in todo) {
        if (todo[key] && isTimeFormat(todo[key])) {
            retData[key] = cvtIsoStringToTime(todo[key]);
        } else {
            retData[key] = todo[key];
        }
    }
    return retData;
}

function getChartData(todos) {
    const columns = [
        { type: 'string', id: 'todo' },
        { type: 'string', id: 'content' },
        { type: 'date', id: 'Start' },
        { type: 'date', id: 'End' },
    ];

    const rows = []
    todos.forEach((todo) => {
        const started_at = getTimeParts(todo.started_at);
        const ended_at = getTimeParts(todo.ended_at);
        if (isValidTodoForChart(todo)) {
            rows.push([
                getTimeTitleByDate(todo.started_at), todo.content, started_at, ended_at
            ]);
        }
    });
    return [columns, ...rows];
}

function isValidTodoForChart(todo) {
    if (!todo.started_at) {
        return false;
    }
    if (!todo.ended_at) {
        return false;
    }
    if (todo.completed === 'N') {
        return false;
    }
    return true;
}

function getTimeTitleByDate(date) {
    const time_parts = date.split('T')
    const ymd = time_parts[0].split('-')
    return `${ymd[1]}-${ymd[2]}`
}

export {
    getTimeNow,
    cvtStringToDate,
    cvtIsoStringToTime,
    cvtTodoToRequestData,
    getChartData,
}
