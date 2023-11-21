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

export {
    getTimeNow,
    cvtStringToDate,
    cvtIsoStringToTime,
    cvtTodoToRequestData,
}