import React from 'react'
import { useParams } from 'react-router-dom'


const TodoItem = ({todo}) => {
    return (
        <tr>
            <td>{todo.id}</td>
            <td>{todo.open}</td>
            <td>{todo.text}</td>
            <td>{todo.data}</td>
            <td>{todo.project}</td>
            <td>{todo.user}</td>
        </tr>
    )
}

const ProjectTodosList = ({todos}) => {
    let { id } = useParams();
    let filtered_todos = todos.filter((todo) => {
        console.log(id)
        console.log(todo.project)
        if (parseInt(id) == todo.project) {
            return todo;
        }
        return;
    });

    return (
        <table>
            <th>
                id
            </th>
            <th>
                open
            </th>
            <th>
                text
            </th>
            <th>
                data
            </th>
            <th>
                project
            </th>
            <th>
                users
            </th>
            {filtered_todos.map((todo) => <TodoItem todo={todo} />)}
        </table>
    )
}

export default ProjectTodosList