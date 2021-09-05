import React from 'react'

const UserItem = ({user}) => {
    return (
        <tr>
            <td>{user.id}</td>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.email}</td>
            <td>{user.username}</td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table>
            <th>
                id
            </th>
            <th>
                First name
            </th>
            <th>
                Last name
            </th>
            <th>
                email
            </th>
            <th>
                Username
            </th>
            {users.map((user) => <UserItem user={user} />)}
        </table>
    )
}

export default UserList