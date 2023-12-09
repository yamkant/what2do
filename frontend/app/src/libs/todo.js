import moment from 'moment-timezone';

const DATE_TIME_FORMAT = 'YYYY-MM-DDTHH:mm:ss';

function cvtStringToYMDString(timeString) {
    if (!timeString) {
        return "";
    }
    const date = moment(timeString).toDate();
    const y = String(date.getFullYear()).padStart(2, '0');
    const m = String(date.getMonth() + 1).padStart(2, '0');
    const d = String(date.getDate()).padStart(2, '0');
    return `${y}-${m}-${d}`;
}

function cvtStringToHMSString(timeString) {
    if (!timeString) {
        return "";
    }
    const date = moment(timeString).toDate();
    const h = String(date.getHours()).padStart(2, '0');
    const m = String(date.getMinutes()).padStart(2, '0');
    const s = String(date.getSeconds()).padStart(2, '0');
    return `${h}:${m}:${s}`;
}

function cvtDateStringToInputDateString(timeString) {
    if (!timeString) {
        return "";
    }
    const date = moment(timeString).toDate();
    const y = String(date.getFullYear()).padStart(2, '0');
    const mo = String(date.getMonth() + 1).padStart(2, '0');
    const d = String(date.getDate()).padStart(2, '0');

    const h = String(date.getHours()).padStart(2, '0');
    const m = String(date.getMinutes()).padStart(2, '0');
    // const s = String(date.getSeconds()).padStart(2, '0');
    return `${y}-${mo}-${d} ${h}:${m}`;
}

function cvtDateToYMDString(date) {
    const tmpStr = date.format(DATE_TIME_FORMAT);
    return tmpStr.split('T')[0]
}

function cvtDateToHMSString(date) {
    const tmpStr = date.format(DATE_TIME_FORMAT);
    return tmpStr.split('T')[1]
}

function cvtDateToHMString(date) {
    const tmpStr = date.format(DATE_TIME_FORMAT);
    const timePart = tmpStr.split('T')[1]
    return timePart.substring(0,timePart.length - 3)
}

function cvtTimeFormatForRequest(dateString, timeString) {
    const formatString = "YYYY-MM-DDTHH:mm:ss";

    const momentObject = moment(dateString + 'T' + timeString, formatString);
    const converted = momentObject.clone().tz('Asia/Seoul').format(formatString);

    return converted;
}

function isTimeFormat(timeString) {
    let offsetPattern = /([+-]\d{2}):(\d{2})$/;
    if (offsetPattern.test(timeString)) {
        return true;
    }
    offsetPattern = /(\d{2}):(\d{2})$/;
    if (offsetPattern.test(timeString)) {
        return true;
    }
    offsetPattern = /^\d{4}-\d{2}-\d{2}T/;
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
            retData[key] = todo[key];
        } else {
            retData[key] = todo[key];
        }
    }
    return retData;
}


export {
    cvtDateToYMDString,
    cvtDateToHMSString,
    cvtDateToHMString,
    cvtDateStringToInputDateString,
    cvtStringToYMDString,
    cvtStringToHMSString,
    cvtTodoToRequestData,
}
