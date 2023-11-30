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

function cvtIsoStringToTime(isoString) {
    if (!isoString) {
        return "";
    }
    const isoTimePart = isoString.split('+')[0]
    const convertedTime = isoTimePart.split('T')[1]
    return convertedTime;
}

function cvtTodoToRequestData(todo) {
    const retData = {}
    // const isoDateTimePattern = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$/;
    const isoDateTimePattern = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2}/;
    for (let key in todo) {
        if (todo[key] && isoDateTimePattern.test(todo[key])) {
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

function getTimeParts(timeString) {
    if (!timeString) {
        return null
    }
    const cvtTimeString = timeString.split('+')[0]
    const time_parts = cvtTimeString.split('T')
    const ymd = time_parts[0].split('-')
    const hms = time_parts[1].split(':')
    // return new Date(ymd[0], ymd[1], ymd[2], hms[0], hms[1], hms[2]);
    return new Date(0, 0, 0, hms[0], hms[1], hms[2]);
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