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
    return isoString.substring(isoString.length - 8, isoString.length - 3);
}

function cvtTodoToRequestData(todo) {
    const retData = {}
    const isoDateTimePattern = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$/;
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
        { type: 'string', id: 'President' },
        { type: 'date', id: 'Start' },
        { type: 'date', id: 'End' },
    ];

    const rows = []
    todos.forEach((todo) => {
        const started_at = getTimeParts(todo.started_at);
        const ended_at = getTimeParts(todo.ended_at);
        if (isValidTodoForChart(todo)) {
            rows.push([
                getTimeTitleByDate(started_at), started_at, ended_at
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
    const time_parts = timeString.split('T')
    const ymd = time_parts[0].split('-')
    const hms = time_parts[1].split(':')
    return new Date(ymd[0], ymd[1], ymd[2], hms[0], hms[1], hms[2]);
}

function getTimeTitleByDate(date) {
    // return `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`
    return `${date.getMonth() + 1}-${date.getDate()}`
}

export {
    getTimeNow,
    cvtStringToDate,
    cvtIsoStringToTime,
    cvtTodoToRequestData,
    getChartData,
}