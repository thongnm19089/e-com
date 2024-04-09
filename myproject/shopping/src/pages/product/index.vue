<template>
  <v-app class="wrap">
    <header class="header">
      <div class="container d-flex items-center justify-between">
        <img alt="Vuetify Logo" class="shrink mr-2" contain
          src="https://lh3.googleusercontent.com/pw/ADCreHd5PMvwKUSbjtSRpUfeyDaazAbdXF1H0arvHtS62AyfivDEAN6hRSq-GTJ6wKiyn-9IEr63aaiNtFq6J2fP_I6VtpGAIwqAQu4B2mL64M2h2HHkPY4VhRWoDpag5VXN3Dxtwb277ZDkXPa0mnDxTTGL=w512"
          transition="scale-transition" height="48px" />

        <v-form class="relative">
          <input class="search-form border-gray border rounded-full" type="text"
            placeholder="Dán link hoặc tìm sản phẩm">
          <div class="search-icon">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" width="24"
              height="24">
              <path data-v-17b6b151="" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
            </svg>
          </div>
        </v-form>

        <div class="d-flex items-center flex-wrap ">
          <div class="menu">
            <div class="bar1"></div>
            <div class="bar2"></div>
            <div class="bar3"></div>
          </div>

          <v-app-bar-title class="uppercase text-16px">Danh mục</v-app-bar-title>
          <v-app-bar-title class="uppercase text-16px">Blog</v-app-bar-title>
        </div>
      </div>
    </header>
    <div class="breadcrumbs">
      <div class="container">
        <v-breadcrumbs style="padding: 0">
          <template v-for="(item, index) in items">
            <v-breadcrumbs-item :href="item.href" :disabled="item.disabled" v-bind:key="index">
              <div v-if="item.icon" v-html="item.icon" class="breadcrumbs-icon text-primary-700"></div>
              <span v-else class="text-sm font-medium whitespace-nowrap text-primary-700" style="color: #4b5563">{{
                item.text }}</span>
            </v-breadcrumbs-item>
            <div class="breadcrumbs-icon" style="margin: 0 16px;" v-bind:key="index" v-if="index < items.length - 1">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"
                class="flex-shrink-0 h-5 w-5 text-gray-600 mr-2 md:mr-4">
                <path fill-rule="evenodd"
                  d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                  clip-rule="evenodd"></path>
              </svg>
            </div>
          </template>
        </v-breadcrumbs>
      </div>
    </div>
    <div class="content" style="margin-top: 96px;">
      <div class="container">
        <v-row>
          <v-col cols="6" style="border: 1px solid rgb(208, 208, 208); padding: 24px 24px 0;" class="relative">
            <div>
              <v-carousel v-model="currentSlide" :show-arrows="false" cycle-controls hide-delimiters>
                <v-carousel-item v-for="(item, i) in product.images" :key="i" :src="item.image" cover aspect-ratio="1">
                </v-carousel-item>
              </v-carousel>
            </div>
            <template>
              <v-sheet class="sub-images mx-auto" elevation="0" max-width="800">
                <div class="carousel-container">
                  <carousel :items="5" :slideToScroll="1" :dots="false" class="relative">
                    <div class="slide" v-for="(image, index) in product.images" :key="index">
                      <v-img :src="image.image" class="product-img" style="width: 90px; height: 90px"
                        @mouseenter="selectImage(index)" :class="{ 'selected': currentSlide === index }">
                      </v-img>
                    </div>
                  </carousel>
                </div>
              </v-sheet>
            </template>
          </v-col>
          <v-col cols="6">
            <h1 class="text-18px">{{ product.title }}</h1>
            <button class="notify">
              <span class="ring"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                  stroke="currentColor" class="shake-bell">
                  <path data-v-959ac308="" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9">
                  </path>
                </svg></span>
              <span class="follow">Theo dõi giảm giá</span>
            </button>
            <p class="d-flex items-center">
              <span>Giá từ</span>
              <span style="margin-left: 4px;">{{ product.store_name }}</span>
              <img class="shoppe-img"
                alt="Shopee"
                :src="product.store_image"
                lazy="loaded">
            </p>
            <div class="price items-center">
              <span class="sp-prince">
                <p class="price-current">{{ formatPrice(product.price_befor) }} ₫</p>
                <p class="price-before">{{ product.price_after ? formatPrice(product.price_after) + ' ₫' : '' }}</p>
              </span>
              <div class="div-tag-price">
                <span class="tag-price" style="margin-left: 4px;"><svg class="svg-img1" data-v-a76bbde4=""
                    xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path data-v-a76bbde4="" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M13 17h8m0 0V9m0 8l-8-8-4 4-6-6"></path>
                  </svg>77.890 ₫</span>
              </div>
              <a href="#">
                <div class="butom-next-shop">
                  <div style="padding-top: 11px;">Đến nơi bán</div>
                  <div style="padding-top: 3px;"><svg style="padding-top: 10px;height: 29px;" data-v-959ac308=""
                      data-v-f089fcd8="" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                      stroke="currentColor" class="ml-1 h-5">
                      <path data-v-959ac308="" data-v-f089fcd8="" stroke-linecap="round" stroke-linejoin="round"
                        stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
                    </svg></div>
                </div>
              </a>
            </div>
            <div class="evaluate">
              <div class="number-rating rating">
                <h4 style="color: #FBBF24;padding-top:7px;">{{ rating }}</h4>
              </div>
              <div class="evaluate-rating rating">
                <template>
                  <div class="d-flex flex-column align-center justify-center">
                    <v-rating v-model="rating" active-color="#FBBF24" color="#FBBF24" half-increments hover
                      size="20"></v-rating>
                    <pre></pre>
                  </div>
                </template>
              </div>
              <div class="number-rating rating">
                <h4 class="evaluate">{{ product.vote ? product.vote + ' Đánh giá' : ' 0 đánh giá ' }}</h4>
              </div>
              <div class="number-rating rating">
                <h4 class="evaluate">{{ product.sales ? product.sales + ' Lượt bán' : ' 0 đánh giá ' }}</h4>
              </div>
            </div>
          </v-col>
          <v-col cols="12" style="padding: 35px  0px;">
            <div class="info-product">
              <template>
                <v-card>
                  <v-tabs v-model="tab" align-tabs="end" color="deep-purple-accent-4">
                    <v-tab :value="1">
                      <div class="icon-svg-tab">
                        <svg data-v-959ac308="" data-v-1fe37343="" height="24" width="24"
                          xmlns="http://www.w3.org/2000/svg">
                          <path data-v-959ac308="" data-v-1fe37343=""
                            d="M8.85 17.93H4.72a2.19 2.19 0 01-.13-.72c0-1.2 2.2-3.84 2.2-3.84S8.97 16 8.97 17.21c0 .26-.06.5-.13.72m-2.07-6.15c-.47 0-.92.21-1.22.58C4.61 13.5 3 15.66 3 17.2a3.79 3.79 0 007.56 0c0-1.55-1.6-3.7-2.56-4.85-.3-.37-.75-.58-1.22-.58m-.04-2.8c.1 0 .2-.03.3-.07l10.53-4.38a.8.8 0 00-.61-1.47L6.44 7.45a.8.8 0 00.3 1.52m12.55 4.6h-4.15a2.17 2.17 0 01-.11-.69c0-1.2 2.19-3.84 2.19-3.84s2.2 2.63 2.2 3.84c0 .24-.06.47-.13.69m-.85-5.55a1.59 1.59 0 00-2.44 0c-.96 1.15-2.56 3.3-2.56 4.86a3.79 3.79 0 007.56 0c0-1.55-1.6-3.7-2.56-4.86"
                            fill="currentColor"></path>
                        </svg>
                      </div>
                      <div>
                        <h3>So sánh giá</h3>
                      </div>
                    </v-tab>
                    <v-tab :value="2">
                      <div class="icon-svg-tab">
                        <svg data-v-959ac308="" data-v-1fe37343="" height="24" width="24"
                          xmlns="http://www.w3.org/2000/svg">
                          <path data-v-959ac308="" data-v-1fe37343=""
                            d="M7.04 16.02a.9.9 0 001.26-.15l2.84-3.6 3.4.52c.35.06.7-.1.9-.4l3.44-5.3a.9.9 0 00-1.5-.97l-3.13 4.82-3.35-.53a.9.9 0 00-.84.33l-3.17 4.02a.9.9 0 00.15 1.26M4.8 19.2V3.9a.9.9 0 10-1.8 0l.01 16.2c0 .5.4.9.9.9h16.2c.5 0 .9-.4.9-.9s-.4-.9-.9-.9H4.8z"
                            fill="currentColor"></path>
                        </svg>
                      </div>
                      <div>
                        <h3>Lịch sử giá</h3>
                      </div>
                    </v-tab>
                    <v-tab :value="3">
                      <div class="icon-svg-tab">
                        <svg data-v-959ac308="" data-v-1fe37343="" height="24" width="24"
                          xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                          <path data-v-959ac308="" data-v-1fe37343=""
                            d="M12 19.4c-4.08 0-7.4-3.32-7.4-7.4S7.92 4.6 12 4.6s7.4 3.32 7.4 7.4-3.32 7.4-7.4 7.4M12 3c-4.962 0-9 4.038-9 9s4.038 9 9 9 9-4.038 9-9-4.038-9-9-9m0 4.577a.9.9 0 00-.9.9v.27a.9.9 0 001.8 0v-.27a.9.9 0 00-.9-.9m0 3.388a.9.9 0 00-.9.899v3.658a.9.9 0 101.8 0v-3.658a.9.9 0 00-.9-.899"
                            fill="currentColor"></path>
                        </svg>
                      </div>
                      <div>
                        <h3>Mô tả sản phẩm</h3>
                      </div>
                    </v-tab>
                    <v-tab :value="4">
                      <div class="icon-svg-tab">
                        <svg data-v-959ac308="" data-v-1fe37343="" height="24" width="24"
                          xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 34 32"
                          stroke="currentColor">
                          <path data-v-959ac308="" data-v-1fe37343=""
                            d="M25.143 13.714q0 2.482-1.679 4.589t-4.58 3.33-6.313 1.223q-1.536 0-3.143-0.286-2.214 1.571-4.964 2.286-0.643 0.161-1.536 0.286h-0.054q-0.196 0-0.366-0.143t-0.205-0.375q-0.018-0.054-0.018-0.116t0.009-0.116 0.036-0.107l0.045-0.089t0.063-0.098 0.071-0.089 0.080-0.089 0.071-0.080q0.089-0.107 0.411-0.446t0.464-0.527 0.402-0.518 0.446-0.688 0.366-0.786q-2.214-1.286-3.482-3.161t-1.268-4q0-2.482 1.679-4.589t4.58-3.33 6.312-1.223 6.313 1.223 4.58 3.33 1.679 4.589zM32 18.286q0 2.143-1.268 4.009t-3.482 3.152q0.179 0.429 0.366 0.786t0.446 0.688 0.402 0.518 0.464 0.527 0.411 0.446q0.018 0.018 0.071 0.080t0.080 0.089 0.071 0.089 0.063 0.098l0.045 0.089t0.036 0.107 0.009 0.116-0.018 0.116q-0.054 0.25-0.232 0.393t-0.393 0.125q-0.893-0.125-1.536-0.286-2.75-0.714-4.964-2.286-1.607 0.286-3.143 0.286-4.839 0-8.429-2.357 1.036 0.071 1.571 0.071 2.875 0 5.518-0.804t4.714-2.304q2.232-1.643 3.429-3.786t1.196-4.536q0-1.375-0.411-2.714 2.304 1.268 3.643 3.179t1.339 4.107z">
                          </path>
                        </svg>
                      </div>
                      <div>
                        <h3>Đánh giá từ người mua</h3>
                      </div>
                    </v-tab>
                  </v-tabs>
                </v-card>
              </template>
            </div>
            <div class="info-product">
              <h3>
                So sánh giá
              </h3>
              <h5>
                Tìm thấy <span class="import">13</span> nơi bán khác, giá từ <span class="import"> 415.000 ₫ - 444.000
                  ₫</span>
              </h5>
            </div>
            <div class="store">
              <div class="logo-store">
                <img
                  src="https://lh3.googleusercontent.com/OwDr2GswbeYne43OtdOL1cqPx_Q7MoXNPbGAAalXumcCojcbb-KcUQqjP4l2EHOPXySoPWqk5YKDcRqT4_22Yv0L0g0NS6owVBz5ZRFCmUEyyC3NcZd4Nndb6vLEkFJ6k29I5fOb=w556-h50-no"
                  alt="">
              </div>
              <div class="list-store">
                <div v-for="(item, index) in product.Shopee" :key="index" class="product-evaluate">
                  <div class="detail-product-evaluatte">
                    <a href="#">
                      <div class="img-product-evaluate">
                        <img class="img-product-evaluate"
                          :src="item.images[0].image" alt="">
                      </div>
                    </a>
                    <div class="container-product-evaluate">
                      <div class="title-product-evaluate">
                        <span class="name-product-evaluate">{{ item.title }}</span>
                        <span class="sale-product-evaluate">{{ item.vote ? item.vote + ' lượt bán' : ''}} lượt bán</span>
                      </div>
                    </div>
                    <div class="price-product-evaluate">
                      <p>{{ formatPrice(item.price_befor) }}</p>
                      <span class="tag-price" style="margin-left: 4px;font-size: 13px;"><svg class="svg-img1"
                          data-v-a76bbde4="" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                          stroke="currentColor">
                          <path data-v-a76bbde4="" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M13 17h8m0 0V9m0 8l-8-8-4 4-6-6"></path>
                        </svg>77.890 ₫</span>
                    </div>
                    <a href="#">
                      <div class="nextpage">
                        <span>Đến nơi bán</span>
                        <svg style="height: 22px;margin-bottom: -6px;" data-v-959ac308="" data-v-f089fcd8=""
                          xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"
                          class="ml-1 h-5">
                          <path data-v-959ac308="" data-v-f089fcd8="" stroke-linecap="round" stroke-linejoin="round"
                            stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
                        </svg>
                      </div>
                    </a>
                  </div>
                </div>
              </div>
            </div>
            <div class="store">
              <div class="logo-store">
                <img style="width: 150px; padding-top: 15px;"
                  src="https://lh3.googleusercontent.com/DF4aF5VZEz_NYkI_eJIyYFD6SM21UyBxiEeWVRaYY3Cr-MUZ8AuUgB6kI6L6DBCzmCJf7TIMRQYdHgZ9m4WEA4e41oglDoWQIpwoK0Tj784azJsPky9g3w6tUR7mhsfi4U8o_NSGJw=w765-h50-no"
                  alt="">
              </div>
              <div class="list-store">
                <div v-for="(item, index) in product.Lazada" :key="index" class="product-evaluate">
                  <div class="detail-product-evaluatte">
                    <a href="#">
                      <div class="img-product-evaluate">
                        <img class="img-product-evaluate"
                          :src="item.images[0].image" alt="">
                      </div>
                    </a>
                    <div class="container-product-evaluate">
                      <div class="title-product-evaluate">
                        <span class="name-product-evaluate">{{ item.title }}</span>
                        <span class="sale-product-evaluate">{{ item.vote ? item.vote + ' lượt bán' : ''}}</span>
                      </div>
                    </div>
                    <div class="price-product-evaluate">
                      <p>{{ formatPrice(item.price_befor) }} ₫</p>
                      <span class="tag-price" style="margin-left: 4px;font-size: 13px;"><svg class="svg-img1"
                          data-v-a76bbde4="" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                          stroke="currentColor">
                          <path data-v-a76bbde4="" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M13 17h8m0 0V9m0 8l-8-8-4 4-6-6"></path>
                        </svg>77.890 ₫</span>
                    </div>
                    <a href="#">
                      <div class="nextpage">
                        <span>Đến nơi bán</span>
                        <svg style="height: 22px;margin-bottom: -6px;" data-v-959ac308="" data-v-f089fcd8=""
                          xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"
                          class="ml-1 h-5">
                          <path data-v-959ac308="" data-v-f089fcd8="" stroke-linecap="round" stroke-linejoin="round"
                            stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
                        </svg>
                      </div>
                    </a>
                  </div>
                </div>
              </div>
            </div>
            <div class="store">
              <div class="logo-store">
                <img style="width: 120px; padding-top: 15px;"
                  src="https://lh3.googleusercontent.com/VaYiFU3XqGRArjLz8nZhSv2VWl39KbeU3Kv3HiK7c5LNA-JqSRZo22Ds2JK0kK04SENns6F8c-vrtQLlC7VHkvh3Y-grYu2HKF6hVAfY0rH_ivBDwdQXB2wc1hkPbBNjp_2Sme5wTA=w515-h50-no"
                  alt="">
              </div>
              <div class="list-store">
                <div v-for="(item, index) in product.Lazada" :key="index" class="product-evaluate">
                  <div class="detail-product-evaluatte">
                    <a href="#">
                      <div class="img-product-evaluate">
                        <img class="img-product-evaluate"
                          :src="item.images[0].image" alt="">
                      </div>
                    </a>
                    <div class="container-product-evaluate">
                      <div class="title-product-evaluate">
                        <span class="name-product-evaluate">{{ item.title }}</span>
                        <span class="sale-product-evaluate">{{ item.vote ? item.vote + ' lượt bán' : ''}}</span>
                      </div>
                    </div>
                    <div class="price-product-evaluate">
                      <p>{{ formatPrice(item.price_befor) }} ₫</p>
                      <span class="tag-price" style="margin-left: 4px;font-size: 13px;"><svg class="svg-img1"
                          data-v-a76bbde4="" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                          stroke="currentColor">
                          <path data-v-a76bbde4="" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M13 17h8m0 0V9m0 8l-8-8-4 4-6-6"></path>
                        </svg>77.890 ₫</span>
                    </div>
                    <a href="#">
                      <div class="nextpage">
                        <span>Đến nơi bán</span>
                        <svg style="height: 22px;margin-bottom: -6px;" data-v-959ac308="" data-v-f089fcd8=""
                          xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"
                          class="ml-1 h-5">
                          <path data-v-959ac308="" data-v-f089fcd8="" stroke-linecap="round" stroke-linejoin="round"
                            stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
                        </svg>
                      </div>
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </v-col>
          <v-col cols="12">
          <template>
            <div>
                        <h3 style="padding-bottom: 30px;">So sánh giá</h3>
            </div>
            <div class=" fill-height align-center justify-center">
              <v-card width = "100%" >
                <v-slide-group >
                  <v-slide-group-item v-for="(item, index) in product.related_products" :key="index" >
                    <v-card  height="420" width="250" >
                      <v-card-title>
                        <div class="container-slide">
                          <div class="img-slide">
                            <img :src="item.src" style="width: 190px;" alt="">
                          </div>
                          <div class="text-info-slide">
                           <div class="div-span-slide"> <span class="sp-title-slide">{{ item.title }}</span></div>
                            <p class="sale-slide">{{ item.sales ? 'Có '+  item.sales + ' Nơi bán' : '' }}</p>
                            <p class="s-slide">Giá Từ {{ formatPrice(item.price_befor) }} ₫</p>
                            <div class="d-flex flex-column align-center justify-center">
                          <v-rating
                            v-model="rating"
                            class="ma-2"
                            density="compact"
                            color="#FBBF24"
                            size="15"
                            active-color="#FBBF24"
                          ></v-rating>
                        </div>
                          </div>
                      </div>
                      </v-card-title>
                    </v-card>
                  </v-slide-group-item>
                </v-slide-group>
              </v-card>
            </div>
          </template>
          </v-col>
          <v-col cols="12" class="banner">
            <div class="text-box box">
              <span class="text">Bạn muốn xem tất cả lịch sử giá của <span>Shopee</span>?!</span>
              <p class="fw400 bottom">Cài đặt ngay Mua Thông Minh Extension phát hiện sale ảo, sale xịn nhé!
              </p>
              <p class="fw400 bottom">Chỉ tốn 3 giây mà siêu tiện, siêu hời!</p>
              <div class="text-box-hover">Thêm Mua Thông Minh vào Chrome/Cốc Cốc</div>
            </div>
            <div class="box">
              <img
                src="https://lh3.googleusercontent.com/KFm2SMk264Yy9KOyJLDzeQ4vveaRN5SbI5sWE5kmZWDiqOAubwyUrThDIpd1__r0mRrNjOOIMJxuEqgGZ_ea1yFOf0_MMZOPgcj5rYTy3W1X29ebwU7EXHI0wvV4PH9xucvfneEAdw=w498-h430-no"
                alt="">
            </div>
          </v-col>
        </v-row>
      </div>
    </div>
    <div class="line">
      <hr class="new4">
    </div>
    <template>
</template>
    <div class="footer container">
      <v-row>
        <v-col cols="12">
          <div class="footer-detail">
            <div class="connect box">
              <img
                src="https://lh3.googleusercontent.com/pw/ADCreHe1uaXgFtO8dlQi1fSrqmcu7OPYJYtSDgXclZin8jZ7oMkHSNc20AqAt7f3wnxrneK1VtZe0s9R7e2476DKCTes06oqHbdx41zz-o15Nf9ggs3HHqGC2K8Ym-dgGvem2sd_03jB8KlUf2MDyq4GOTH_=w256"
                alt="">
              <p class="text bottom fw400">Mua Thông Minh là website, ứng dụng tìm kiếm và đánh giá hàng hóa sản phẩm
                online. Giúp bạn né Sale ảo, mua giá tốt, tin cậy và trở thành người tiêu dùng thông thái.<span
                  class="text2 bottom fw600">MuaThongMinh.vn không bán hàng!</span></p>
              <p class="text1 bottom">KẾT NỐI VỚI CHÚNG TÔI</p>
              <div class="icon-fb-img">
                <div class="icon box"><svg data-v-68c915d5="" fill="currentColor" viewBox="0 0 24 24"
                    aria-hidden="true">
                    <path data-v-68c915d5="" fill-rule="evenodd"
                      d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z"
                      clip-rule="evenodd"></path>
                  </svg></div>
                <div class="icon box"><svg data-v-68c915d5="" fill="currentColor" viewBox="0 0 24 24"
                    aria-hidden="true">
                    <path data-v-68c915d5="" fill-rule="evenodd"
                      d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 015.45 2.525c.636-.247 1.363-.416 2.427-.465C8.901 2.013 9.256 2 11.685 2h.63zm-.081 1.802h-.468c-2.456 0-2.784.011-3.807.058-.975.045-1.504.207-1.857.344-.467.182-.8.398-1.15.748-.35.35-.566.683-.748 1.15-.137.353-.3.882-.344 1.857-.047 1.023-.058 1.351-.058 3.807v.468c0 2.456.011 2.784.058 3.807.045.975.207 1.504.344 1.857.182.466.399.8.748 1.15.35.35.683.566 1.15.748.353.137.882.3 1.857.344 1.054.048 1.37.058 4.041.058h.08c2.597 0 2.917-.01 3.96-.058.976-.045 1.505-.207 1.858-.344.466-.182.8-.398 1.15-.748.35-.35.566-.683.748-1.15.137-.353.3-.882.344-1.857.048-1.055.058-1.37.058-4.041v-.08c0-2.597-.01-2.917-.058-3.96-.045-.976-.207-1.505-.344-1.858a3.097 3.097 0 00-.748-1.15 3.098 3.098 0 00-1.15-.748c-.353-.137-.882-.3-1.857-.344-1.023-.047-1.351-.058-3.807-.058zM12 6.865a5.135 5.135 0 110 10.27 5.135 5.135 0 010-10.27zm0 1.802a3.333 3.333 0 100 6.666 3.333 3.333 0 000-6.666zm5.338-3.205a1.2 1.2 0 110 2.4 1.2 1.2 0 010-2.4z"
                      clip-rule="evenodd"></path>
                  </svg></div>
                <div class="icon box"><svg data-v-68c915d5="" fill="currentColor" viewBox="0 0 24 24"
                    aria-hidden="true">
                    <path data-v-68c915d5="" fill-rule="evenodd"
                      d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"
                      clip-rule="evenodd"></path>
                  </svg></div>
              </div>
            </div>
            <div class="info-div box">
              <p class="info-p fw600 op70">VỀ MUA THÔNG MINH</p>
              <p class="info-p fw400">Blog</p>
              <p class="info-p fw400">Giới thiệu</p>
              <p class="info-p fw400">Chính sách bảo mật</p>
              <p class="info-p fw400">Điều khoản sử dụng</p>
              <p class="info-p fw400">Metric</p>
              <p class="info-p fw400">Điểm thi</p>
            </div>
            <div class="contact">
              <p class="info-p fw600 op70">LIÊN HỆ</p>
              <p class="info-p fw400">Công ty Cổ phần Khoa học Dữ liệu</p>
              <p class="info-p fw400">Địa chỉ: Tầng 6 toà nhà AZ Lâm Viên, 107A Nguyễn Phong Sắc, Phường Dịch Vọng Hậu,
                Quận
                Cầu Giấy, Thành phố Hà Nội, Việt Nam.</p>
              <p class="info-p fw400">Email: info@beecost.com</p>
            </div>
          </div>
          <div class="line1">
            <hr class="new5">
          </div>
          <div class="area box">
            <span class="area-sp">Quốc gia & Khu vực:</span>
            <a href="#"><span class="area-sp">Việt Nam</span></a>
            <a href="#"><span class="area-sp border-one">Singapore</span></a>
            <a href="#"><span class="area-sp border-one">Philippines</span></a>
            <a href="#"><span class="area-sp border-one">Malaysia</span></a>
            <a href="#"><span class="area-sp border-one">Indonesia</span></a>
            <a href="#"><span class="area-sp border-one">Đài Loan</span></a>
            <a href="#"><span class="area-sp border-one">Mexico</span></a>
            <a href="#"><span class="area-sp border-one">Brazil</span></a>
            <a href="#"><span class="area-sp border-one">Thái Lan</span></a>
          </div>
        </v-col>
      </v-row>
    </div>
  </v-app>
</template>

<script>
import carousel from 'vue-owl-carousel'
import axios from 'axios'

export default {
  name: 'Product',
  components: { carousel },
  data () {
    return {
      product: {},
      priceBefore: null,
      priceAfter: null,
      itemSize: 4,
      rating: 4.9,
      currentSlide: 0,
      next: '-123',
      items: [
        { icon: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="flex-shrink-0 h-5 w-5"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path></svg>', disabled: false, href: '/' },
        { text: 'Máy tính & Laptop', disabled: false, href: '/page1' },
        { text: 'Phụ Kiện Máy Tính', disabled: false, href: '/page1' },
        { text: 'Bộ chia cổng USB & Đọc thẻ nhớ', disabled: true }
      ],
      images: [
        { 'src': 'https://cf.shopee.vn/file/38625d8696c075b0266676b87dc910dd_tn' },
        { 'src': 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg' },
        { 'src': 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg' },
        { 'src': 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg' },
        { 'src': 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg' },
        { 'src': 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg' },
        { 'src': 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg' }
      ]
    }
  },
  async created () {
    axios.get(`http://127.0.0.1:8000/api/products/${this.$route.params.id}`)
      .then(response => {
        this.product = response.data
        this.priceBefore = this.product.price_before
        this.priceAfter = this.product.price_after
      }).catch(error => {
        console.log('error', error)
        return this.$router.push('/404')
      })
  },
  mounted () {
  },
  methods: {
    formatPrice (value) {
      let val = (value / 1).toFixed(0).replace('.', ',')
      return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, '.')
    },
    selectImage (index) {
      this.currentSlide = index
    },
    amountReduced () {
      if (this.priceAfter !== null) {
        return this.priceAfter - this.pe
      } else {
        return 0
      }
    }
  }
}
</script>

<style scoped>
.slide{
  display: inline-block;
}
.s-slide{
  color: red;
  font-size: 15px;
  font-weight: 500;
  margin-bottom: 0px;
}
.div-span-slide{
  height: 90px;
}
.sale-slide{
  color: rgb(1, 110, 74);
  background-color: #c5fce2;
  padding: 5px 5px;
  font-weight: 500;
  margin: 7px 2px;
  width: 55%;
  border-radius: 6px;
  bottom: 10px;

}
.text-info-slide{
  font-size: 13px;
  line-height: 1.5;
  font-weight: 400;
  padding: 0 10px;
  height: 180px;
}
.sp-title-slide:hover{
  color: red;
}
.area {
  text-align: center;
  font-size: 88%;
  padding-bottom: 40px;
  letter-spacing: 0.4px;
}

.area-sp {
  padding-left: 11px;
  color: #000000;
}

a {
  text-decoration: none;
}

.border-one {
  border-left: #c4c4c4 solid 1px;
  ;
}

.op70 {
  opacity: 70%;
}

.info-p {
  margin-bottom: 15px;
  font-size: 15.5px;
  padding-left: 40px;
  opacity: 80%;
}

.icon-fb-img {
  display: flex;
}

.icon {
  width: 25px;
  margin-right: 30px;
  opacity: 50%;
  margin-left: 5px;
}

.box p.text1 {
  margin-bottom: 0;
  padding-right: 10px;
  padding: 10px 0px;
}

.text2 {
  margin-bottom: 0;
  padding-right: 10px;
  padding: 10px 0px;
  font-size: 16px;
}

.box p.text {
  margin-bottom: 0;
  padding-right: 10px;
}

.footer-detail {
  display: flex;
}

.connect {
  width: 40%;
  opacity: 80%;
}

.info-div {
  width: 30%;
  padding-right: 10px;
  padding-top: 5px;
}

.contact {
  width: 40%;
  padding-top: 5px;
}

.line {
  padding-top: 80px;
  padding-bottom: 30px;
}

.line1 {
  padding: 15px 0px;
}

hr.new4 {
  border: 2px solid #FF7227;
}

hr.new5 {
  border: 1px solid #b9b9b9;
}

.banner {
  background: rgba(35, 104, 212, 0.2);
  height: 458px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  border-radius: 10px;
  margin-top: 30px;
}

.box {
  display: block;
}

.text-box-hover {
  font-weight: 500;
  letter-spacing: 0.8px;
  padding: 15px 20px;
  background-color: #FF7227;
  border-radius: 10px;
  color: white;
  line-height: 1.6;
  margin-top: 30px;
}

.text-box {
  padding: 60px 80px;

}

.fw600 {
  font-weight: 600;
}

p.fw400 {
  font-weight: 400;
}

.box span.text {
  font-size: 25px;
  font-weight: bold;
}

.box .bottom {
  padding-top: 7px;
  padding-right: 34px;
  letter-spacing: 1px;
}

.box span span {
  color: #FF7227;
}

.title-product-evaluate {
  display: block;
}

.nextpage {
  display: block;
  float: inline-end;
  border: 1px solid;
  padding: 8px 23px;
  border-radius: 5px;
  display: block;
  height: 44px;
  margin-top: 24px;
  color: #1B5AF2;
}

.nextpage:hover {
  background-color: #1B5AF2;
  color: #E8EAED;
  font-weight: bold;
}

.center-icon {
  display: inline-block;
}

.name-product-evaluate {
  width: 670px;
  padding-right: 100px;
  padding-left: 15px;
  padding-top: 15px;
  display: block;
  line-height: 1.4;
  font-weight: 400;
}

.name-product-evaluate:hover {
  color: #FF7227;
}

.sale-product-evaluate {
  padding-left: 15px;
  display: block;
  font-size: 13px;
  padding-top: 5px;
}

.price-product-evaluate p {
  color: red;
  width: 106px;
  margin: auto;
  padding-top: 35px;
  padding-left: 7px;
  letter-spacing: 0.8px;
  font-weight: 500;
}

.img-product-evaluate {
  width: 80px;
  height: 80px;
  padding: 10px;
}

.detail-product-evaluatte {
  display: flex;
}

.product-evaluate {
  height: 115px;
  border-radius: 13px;
  padding-top: 10px;
  box-shadow:
    2px 2px 2px 0px #EBF4F3,
    0px 2px 2px 0px rgba(0, 222, 230, 0.5),
    2px 2px 2px 0px rgba(176, 224, 230, 0.5);
  transition: box-shadow 0.3s ease;
  margin-top: 15px;
}

.product-evaluate:hover {
  box-shadow:
    -3px 3px 6px 0px rgba(118, 173, 177, 0.8),
    0px 0px 6px 0px rgba(137, 196, 204, 0.8),
    3px 3px 6px 0px rgba(176, 224, 230, 0.8),
    0px 0px 6px 0px rgba(107, 182, 187, 0.8);
}

.container {
  margin-left: auto;
  margin-right: auto;
  width: 1040px !important;
}

.logo-store {
  padding-top: 10px;
}

.info-product {
  padding: 12px 0px;
}

.import {
  font-weight: 900;
}

h5 {
  font-size: 15px;
  font-weight: 300;
  padding-top: 15px;
}

.icon-svg-tab {
  padding-right: 7px;
}

h4.evaluate {
  padding: 0px 5px;
  border-left: #E8EAED solid 2px;
  margin-top: 7px;
  font-size: 15px;
  font-weight: 400;
}

.butom-next-shop {
  background-color: #FF7227;
  border-radius: 6px;
  padding-bottom: 6px;
  margin-left: 60px;
  padding-right: 24px;
  padding-left: 26px;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  float: inline-start;
  color: white;

}

.div-tag-price {
  float: inline-start;
}

.rating {
  float: inline-start;
}

.tag-price {
  background-color: #A7F3D0;
  border-radius: 8px;
  padding: 3px 5px;
  margin-top: 50px;
}

.tag-price:hover {
  text-decoration: underline;
}

.svg-img1 {
  width: 17px;
  margin-right: 6px;
  margin-bottom: -3px;

}

.price-current {
  color: red;
  font-weight: 700;
  font-size: 27px;
  margin-bottom: 1px;
}

.price-before {
  font-size: 14px;
  text-decoration: line-through;
}

.price {
  display: flex;
}

.sp-prince {
  float: inline-start;
  padding-right: 50px;
}

.d-flex {
  display: flex;
}

.items-center {
  align-items: center;
}

.flex-wrap {
  flex-wrap: wrap;
}

.justify-between {
  justify-content: space-between;
}

.uppercase {
  text-transform: uppercase;
}

.text-16px {
  font-size: 16px;
}

.text-18px {
  font-size: 18px;
}

.header {
  height: 81px;
  border: 1px solid rgba(209, 213, 219, 0.5);
}

.search-form {
  width: 576px;
  height: 40px;
  border-radius: 9999px;
  border: 1px solid rgba(209, 213, 219, 1);
  padding: 0 80px 0 20px;
}

.search-icon {
  position: absolute;
  top: 0;
  right: 0;
  height: 40px;
  width: 48px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: rgba(255, 114, 39, 1);
}

.relative {
  position: relative !important;
}

.product-img {
  border: 1px solid;
  border-color: rgba(229, 231, 235, 1);
}

.menu {
  display: inline-block;
  cursor: pointer;
  margin-right: 8px;
}

.bar1,
.bar2,
.bar3 {
  width: 20px;
  height: 2px;
  background-color: #000000;
  margin: 4px 0;
  transition: 0.4s;
}

.header .v-app-bar-title:last-child {
  margin-left: 16px;
}

.breadcrumbs-icon {
  width: 20px;
  height: 20px;
}

.font-medium {
  font-weight: 500;
}

.text-sm {
  font-size: .875rem;
  line-height: 1.25rem;
}

.whitespace-nowrap {
  white-space: nowrap;
}

.breadcrumbs .text-primary-700:hover {
  color: rgba(199, 65, 16, 1) !important;
}

.v-carousel__item {
  width: 470px;
  height: 470px;
}

.sub-images .selected {
  border: 2px solid rgba(245, 152, 56, 1);
}

.slick-next,
.slick-prev {
  border: none;
  cursor: pointer;
  display: block;
  font-size: 0;
  height: 20px;
  line-height: 0;
  padding: 0;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 20px;
}

.carousel-container {
  position: relative;
}

.notify {
  display: flex;
  width: 11rem;
  padding-left: .5rem;
  padding-right: .5rem;
  padding-bottom: .25rem;
  padding-top: .25rem;
  margin-bottom: 1rem;
  margin-top: 1rem;
  border: 1px solid rgba(255, 114, 39, 1);
  border-radius: 1rem;
  align-items: center;
  color: rgba(255, 114, 39, 1);
  font-weight: 500;
  cursor: pointer;
}

.notify:hover {
  color: rgba(255, 255, 255, 1);
  background-color: rgba(255, 114, 39, 1);
}

.ring {
  height: 1.25rem;
}

.shake-bell {
  height: 1.25rem;
  animation: ring-959ac308 4s ease-in-out .7s infinite;
  transform-origin: 50% 4px;
}

@keyframes ring-959ac308 {
  0% {
    transform: rotate(0)
  }

  1% {
    transform: rotate(30deg)
  }

  3% {
    transform: rotate(-28deg)
  }

  5% {
    transform: rotate(34deg)
  }

  7% {
    transform: rotate(-32deg)
  }

  9% {
    transform: rotate(30deg)
  }

  11% {
    transform: rotate(-28deg)
  }

  13% {
    transform: rotate(26deg)
  }

  15% {
    transform: rotate(-24deg)
  }

  17% {
    transform: rotate(22deg)
  }

  19% {
    transform: rotate(-20deg)
  }

  21% {
    transform: rotate(18deg)
  }

  23% {
    transform: rotate(-16deg)
  }

  25% {
    transform: rotate(14deg)
  }

  27% {
    transform: rotate(-12deg)
  }

  29% {
    transform: rotate(10deg)
  }

  31% {
    transform: rotate(-8deg)
  }

  33% {
    transform: rotate(6deg)
  }

  35% {
    transform: rotate(-4deg)
  }

  37% {
    transform: rotate(2deg)
  }

  39% {
    transform: rotate(-1deg)
  }

  41% {
    transform: rotate(1deg)
  }

  43% {
    transform: rotate(0)
  }

  to {
    transform: rotate(0)
  }
}

.shoppe-img {
  border-radius: 9999px;
  height: 32px;
  margin-left: 12px;
}
</style>
