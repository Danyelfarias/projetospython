import React, { useState, useEffect } from 'react';
import axios from 'axios';

function SharePointList() {
  const [listItems, setListItems] = useState([]);

  useEffect(() => {
    async function fetchListItems() {
      try {
        const response = await axios.get(
          'https://<seu_site>.sharepoint.com/sites/<seu_site>/<sua_lista>/_api/web/lists/getbytitle(\'<sua_lista>\')/items',
          {
            headers: {
              Accept: 'application/json;odata=verbose',
            },
            auth: {
              username: '<seu_email>',
              password: '<sua_senha>',
            },
          }
        );
        setListItems(response.data.d.results);
      } catch (error) {
        console.error(error);
      }
    }

    fetchListItems();
  }, []);

  async function handleAddItem() {
    try {
      const response = await axios.post(
        'https://<seu_site>.sharepoint.com/sites/<seu_site>/<sua_lista>/_api/web/lists/getbytitle(\'<sua_lista>\')/items',
        {
          __metadata: { type: 'SP.Data.<sua_lista>ListItem' },
          Title: 'Novo Item',
          Description: 'Descrição do Novo Item',
        },
        {
          headers: {
            Accept: 'application/json;odata=verbose',
            'Content-Type': 'application/json;odata=verbose',
          },
          auth: {
            username: '<seu_email>',
            password: '<sua_senha>',
          },
        }
      );
      setListItems([...listItems, response.data.d]);
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <div>
      <h2>Itens da Lista:</h2>
      <ul>
        {listItems.map((item) => (
          <li key={item.ID}>{item.Title} - {item.Description}</li>
        ))}
      </ul>
      <button onClick={handleAddItem}>Adicionar Item</button>
    </div>
  );
}

export default SharePointList;
