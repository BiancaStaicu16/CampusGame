// This page should show the cards that the user has collected 

<template>
  <div class="page-main">
    <h1>My Cards</h1>
    <div class="page-content">
      <div class="card">
        <div class="content">
          {% for card in cards %}
          <h2 class="title">{{ card[cardName] }}</h2>
          <p class="copy">
            {{ card[cardValue] }}
          </p>
          {% end for %}
        </div>
      </div>
    </div>
  </div>
</template>


