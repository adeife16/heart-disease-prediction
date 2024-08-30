<template>
  <div id="app" class="app-container">
    <h1>Cardiomegaly Detection</h1>
    <label for="file-upload" class="custom-file-upload">
      Choose Image
    </label>
    <input type="file" id="file-upload" @change="onFileChange" />
    <button @click="uploadImage" class="upload-button">
      Upload and Predict
    </button>
    <img v-if="selectedFile" :src="imagePreview" alt="Uploaded Image" class="preview-image" />
    <p v-if="prediction">Heart Disease Detection is: {{ prediction }}</p>
    <p v-if="confidence">Model confidence is: {{ confidence }}%</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      selectedFile: null,
      prediction: null,
      confidence: null,
      imagePreview: null,
    };
  },
  methods: {
    onFileChange(event) {
      this.selectedFile = event.target.files[0];
      this.imagePreview = URL.createObjectURL(this.selectedFile);
    },
    async uploadImage() {
      if (!this.selectedFile) return;
      const formData = new FormData();
      if (!this.selectedFile.type.match('image.*')) {
        alert('The file type is not supported. Please choose a valid image file.');
        return;
      }
      // if no image was uploaded
      if (!this.selectedFile) {
        alert('Please select an image file to upload.');
        return;
      }
      formData.append('image', this.selectedFile);

      try {
        const response = await axios.post('http://127.0.0.1:5000/predict', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
        this.prediction = response.data.prediction;
        this.confidence = response.data.confidence;
      } catch (error) {
        console.error('Error uploading the image:', error);
        this.prediction = 'Error occurred while processing the image.';
      }
    },
  },
};
</script>

<style scoped>
.app-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background-color: #f0f8ff; /* Light blue background for a cool color scheme */
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h1 {
  color: #1e90ff; /* Dodger blue color for the heading */
  margin-bottom: 20px;
}

.custom-file-upload {
  display: inline-block;
  background-color: #1e90ff; /* Matching the heading color */
  color: white;
  padding: 10px 20px;
  cursor: pointer;
  border-radius: 5px;
  margin-bottom: 20px;
  transition: background-color 0.3s ease;
}

.custom-file-upload:hover {
  background-color: #187bcd; /* Slightly darker blue on hover */
}

#file-upload {
  display: none; /* Hide the original file input */
}

.upload-button {
  background-color: #4caf50; /* Green button */
  color: white;
  padding: 14px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-bottom: 20px;
  transition: background-color 0.3s ease;
}

.upload-button:hover {
  background-color: #45a049; /* Darker green on hover */
}

.preview-image {
  max-width: 300px;
  max-height: 300px;
  margin-bottom: 20px;
  border-radius: 5px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

p {
  color: #333; /* Dark text for contrast */
  font-size: 16px;
  margin-bottom: 10px;
}
</style>
