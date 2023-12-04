export default class GChartHelper {
    constructor(dateObj, todos) {
        this.dateObj = dateObj;
        this.todos = todos;
    }

    getChartData() {
        const columns = [
            { type: 'string', id: 'todo' },
            { type: 'string', id: 'content' },
            { type: 'date', id: 'Start' },
            { type: 'date', id: 'End' },
        ];

        const rows = []
        this.todos.forEach((todo) => {
            const started_at = this.cvtTimeStringToHMSDate(todo.started_at);
            const ended_at = this.cvtTimeStringToHMSDate(todo.ended_at);
            if (this.isValidTodoForChart(todo)) {
                rows.push([
                    this.getTimeTitleByDate(todo.started_at), todo.content, started_at, ended_at
                ]);
            }
        });
        return [columns, ...rows];
    }

    isValidTodoForChart(todo) {
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

    getTimeTitleByDate(date) {
        const time_parts = date.split('T')
        const ymd = time_parts[0].split('-')
        return `${ymd[1]}-${ymd[2]}`
    }

    cvtTimeStringToHMSDate(timeString) {
        if (!timeString) {
            return null
        }
        const date = this.dateObj(timeString).toDate();
        const h = date.getHours();
        const m = date.getMinutes();
        const s = date.getSeconds();
        return new Date(0, 0, 0, h, m, s);
    }

}