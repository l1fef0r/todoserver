import React from 'react'

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

const TodoList = ({todos}) => {
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
                user
            </th>
            {todos.map((todo) => <TodoItem todo={todo} />)}
        </table>
    )
}

export default TodoList