<template>
	<div class="grid-container">
		<div class="title">
			<h1>Garages</h1>
			<new-garage @change="addGarage"></new-garage>

		</div>
		<ul class="list-group">
		    <li v-for="g in garageList" class="list-group-item" :key="g.id">
				<!-- when a garage item is deleted it will raise change event and return the new list -->
				<garage-list-item :garage="g" @change-delete="deleteGarage">hello</garage-list-item>
			</li>
		</ul>

		<router-link to="/mitko">To About</router-link>
	</div>
</template>

<script>
    import GarageListItem from "./garage-list-item";
    import GarageForm from "./garage-form";
	import NewGarage from "./new-garage";

	export default {
		name: 'garage-list',
		components: {NewGarage, GarageListItem, GarageForm},
		data: function () {
			return {
				garageList: [],
                garageDialog: true,
			}
		},
		methods: {
			load() {
				$.ajax({
					type: 'GET',
					url: `/garages/`,
					contentType: 'application/json',
					timeout: 60000
				}).then((data) => {
					console.log(data)
					this.garageList = data
				}).always(() => {
					// this.loading = false
				})
			},

			addGarage(garage_data) {
				console.log("Event: ", garage_data);
				this.garageList.push(garage_data)
			},

			deleteGarage(id)
			{
				this.garageList = this.garageList.filter((gar) => gar.id !== id);
			}
		},
		created: function() {
			console.log('created!');
			this.load();
		}
	}

</script>

<style scoped>
	.grid-container {
		display: grid;
		grid-template-columns: 2fr 6fr;
		grid-gap: 10px;
		grid-auto-rows: min-content;
		grid-template-areas:
			"title garage-list ";
	}

	.title {
        grid-area: title;
		margin-right: 20px;
    }
	.list-group {
        grid-area: garage-list;
    }
    .add-garage {
        margin: 4px;
    }

</style>
