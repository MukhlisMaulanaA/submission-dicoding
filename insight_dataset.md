<div class="markdown prose w-full break-words dark:prose-invert dark">
  <h2>Insight Dataset E-Commerce</h2>
  <h3>1. <strong>Customer Data (<code>customer_data</code>)</strong></h3>
  <ul>
    <li><strong>Deskripsi:</strong> Dataset ini berisi informasi tentang pelanggan seperti ID unik, lokasi pelanggan
      (kode pos, kota, negara bagian).</li>
    <li><strong>Kolom Utama:</strong>
      <ul>
        <li><code>customer_id</code>: ID pelanggan yang bisa dihubungkan dengan transaksi.</li>
        <li><code>customer_unique_id</code>: ID unik untuk mengidentifikasi pelanggan.</li>
        <li><code>customer_zip_code_prefix</code>: Kode pos pelanggan.</li>
        <li><code>customer_city</code>: Kota pelanggan.</li>
        <li><code>customer_state</code>: Negara bagian tempat tinggal pelanggan.</li>
      </ul>
    </li>
    <li><strong>Potensi Insight:</strong> Ini bisa digunakan untuk analisis geografis (misalnya distribusi pelanggan),
      segmentasi pelanggan berdasarkan wilayah, atau korelasi antara lokasi pelanggan dan frekuensi pembelian.</li>
  </ul>
  <h3>2. <strong>Geolocation Data (<code>geo_data</code>)</strong></h3>
  <ul>
    <li><strong>Deskripsi:</strong> Dataset ini berisi informasi lokasi geografis berdasarkan kode pos, termasuk
      koordinat (latitude, longitude) serta nama kota dan negara bagian.</li>
    <li><strong>Kolom Utama:</strong>
      <ul>
        <li><code>geolocation_zip_code_prefix</code>: Kode pos yang bisa dihubungkan dengan data pelanggan atau penjual.
        </li>
        <li><code>geolocation_lat</code>, <code>geolocation_lng</code>: Koordinat geografis untuk memetakan lokasi.</li>
        <li><code>geolocation_city</code>: Nama kota.</li>
        <li><code>geolocation_state</code>: Negara bagian lokasi.</li>
      </ul>
    </li>
    <li><strong>Potensi Insight:</strong> Dapat digunakan untuk melakukan visualisasi geografis dari penjualan atau
      distribusi pelanggan/penjual, serta membantu dalam mengoptimalkan pengiriman dan logistik.</li>
  </ul>
  <h3>3. <strong>Order Item Data (<code>order_item_data</code>)</strong></h3>
  <ul>
    <li><strong>Deskripsi:</strong> Dataset ini berisi detail barang yang dipesan, termasuk ID pesanan, produk, harga,
      biaya pengiriman, dan tenggat waktu pengiriman.</li>
    <li><strong>Kolom Utama:</strong>
      <ul>
        <li><code>order_id</code>: ID pesanan untuk menghubungkan dengan transaksi lainnya.</li>
        <li><code>product_id</code>: ID produk yang dibeli.</li>
        <li><code>price</code>: Harga produk yang dibeli.</li>
        <li><code>freight_value</code>: Biaya pengiriman.</li>
        <li><code>shipping_limit_date</code>: Batas waktu pengiriman.</li>
      </ul>
    </li>
    <li><strong>Potensi Insight:</strong> Dataset ini penting untuk analisis produk terlaris, tren harga, dan dampak
      biaya pengiriman terhadap pembelian.</li>
  </ul>
  <h3>4. <strong>Order Payments Data (<code>order_payments_data</code>)</strong></h3>
  <ul>
    <li><strong>Deskripsi:</strong> Dataset ini menyimpan informasi pembayaran untuk setiap pesanan, termasuk jenis
      pembayaran dan nilai pembayaran.</li>
    <li><strong>Kolom Utama:</strong>
      <ul>
        <li><code>order_id</code>: ID pesanan untuk menghubungkan dengan data pesanan lainnya.</li>
        <li><code>payment_type</code>: Jenis metode pembayaran yang digunakan (misalnya kartu kredit, transfer).</li>
        <li><code>payment_installments</code>: Jumlah cicilan yang digunakan pelanggan.</li>
        <li><code>payment_value</code>: Nilai total pembayaran.</li>
      </ul>
    </li>
    <li><strong>Potensi Insight:</strong> Bisa digunakan untuk analisis popularitas metode pembayaran, serta hubungan
      antara metode pembayaran dan nilai transaksi.</li>
  </ul>
  <h3>5. <strong>Order Reviews Data (<code>order_reviews_data</code>)</strong></h3>
  <ul>
    <li><strong>Deskripsi:</strong> Berisi ulasan pelanggan mengenai produk yang dibeli, termasuk skor dan pesan ulasan.
    </li>
    <li><strong>Kolom Utama:</strong>
      <ul>
        <li><code>review_id</code>: ID ulasan.</li>
        <li><code>order_id</code>: ID pesanan terkait ulasan.</li>
        <li><code>review_score</code>: Skor ulasan (misalnya dari 1 hingga 5).</li>
        <li><code>review_comment_message</code>: Isi pesan ulasan dari pelanggan.</li>
        <li><code>review_creation_date</code>: Tanggal ulasan dibuat.</li>
      </ul>
    </li>
    <li><strong>Potensi Insight:</strong> Ini dapat digunakan untuk analisis kepuasan pelanggan, dampak ulasan terhadap
      penjualan, serta pengelompokan produk berdasarkan rating yang diterima.</li>
  </ul>
  <h3>6. <strong>Orders Data (<code>orders_data</code>)</strong></h3>
  <ul>
    <li><strong>Deskripsi:</strong> Dataset ini menyimpan informasi tentang pesanan yang dilakukan oleh pelanggan,
      termasuk status pesanan dan tanggal penting.</li>
    <li><strong>Kolom Utama:</strong>
      <ul>
        <li><code>order_id</code>: ID pesanan.</li>
        <li><code>customer_id</code>: ID pelanggan yang melakukan pemesanan.</li>
        <li><code>order_status</code>: Status pesanan (misalnya delivered, shipped).</li>
        <li><code>order_purchase_timestamp</code>: Waktu pembelian dilakukan.</li>
        <li><code>order_delivered_customer_date</code>: Tanggal pesanan diterima pelanggan.</li>
      </ul>
    </li>
    <li><strong>Potensi Insight:</strong> Penting untuk analisis tren penjualan dari waktu ke waktu, durasi pengiriman,
      dan segmentasi pelanggan berdasarkan frekuensi dan nilai pesanan.</li>
  </ul>
  <h3>7. <strong>Product Data (<code>product_data</code>)</strong></h3>
  <ul>
    <li><strong>Deskripsi:</strong> Dataset ini berisi informasi tentang produk yang dijual, termasuk kategori produk,
      panjang nama, deskripsi, jumlah foto, dan dimensi produk.</li>
    <li><strong>Kolom Utama:</strong>
      <ul>
        <li><code>product_id</code>: ID produk yang bisa dihubungkan dengan penjualan.</li>
        <li><code>product_category_name</code>: Kategori produk.</li>
        <li><code>product_photos_qty</code>: Jumlah foto produk.</li>
        <li><code>product_weight_g</code>: Berat produk dalam gram.</li>
        <li><code>product_length_cm</code>, <code>product_height_cm</code>, <code>product_width_cm</code>: Dimensi
          produk.</li>
      </ul>
    </li>
    <li><strong>Potensi Insight:</strong> Bisa digunakan untuk analisis produk terlaris dan pengaruh dimensi atau foto
      produk terhadap penjualan.</li>
  </ul>
  <h3>8. <strong>Sellers Data (<code>sellers_data</code>)</strong></h3>
  <ul>
    <li><strong>Deskripsi:</strong> Dataset ini menyimpan informasi tentang penjual, termasuk lokasi mereka.</li>
    <li><strong>Kolom Utama:</strong>
      <ul>
        <li><code>seller_id</code>: ID penjual.</li>
        <li><code>seller_zip_code_prefix</code>: Kode pos penjual.</li>
        <li><code>seller_city</code>: Kota penjual.</li>
        <li><code>seller_state</code>: Negara bagian penjual.</li>
      </ul>
    </li>
    <li><strong>Potensi Insight:</strong> Dapat digunakan untuk analisis performa penjual, distribusi geografis penjual,
      dan hubungan antara lokasi penjual dan kecepatan pengiriman.</li>
  </ul>
  <h3>9. <strong>Product Category Data (<code>product_category_data</code>)</strong></h3>
  <ul>
    <li><strong>Deskripsi:</strong> Dataset ini berisi hubungan antara nama kategori produk dalam bahasa asli dan
      terjemahannya ke dalam bahasa Inggris.</li>
    <li><strong>Kolom Utama:</strong>
      <ul>
        <li><code>product_category_name</code>: Nama kategori dalam bahasa asli.</li>
        <li><code>product_category_name_english</code>: Nama kategori dalam bahasa Inggris.</li>
      </ul>
    </li>
    <li><strong>Potensi Insight:</strong> Penting untuk memahami dan mengelompokkan produk berdasarkan kategori saat
      menganalisis penjualan per kategori.</li>
  </ul>
  <hr>
  <h3>Kesimpulan Awal dari Insight:</h3>
  <ul>
    <li><strong>Customer-Centric Analysis:</strong> Dataset ini menyediakan informasi yang cukup untuk melakukan
      analisis berbasis pelanggan, baik untuk melihat distribusi geografis pelanggan, frekuensi pembelian, hingga ulasan
      produk.</li>
    <li><strong>Product-Centric Analysis:</strong> Data produk dan pesanan dapat memberikan insight mengenai produk
      terlaris, kategori yang paling laris, dan produk dengan potensi untuk lebih dipromosikan.</li>
    <li><strong>Operational Analysis:</strong> Melalui data pengiriman, kita bisa menganalisis efektivitas logistik dan
      pengaruhnya terhadap kepuasan pelanggan.</li>
    <li><strong>Segmentasi Pelanggan:</strong> Dataset memungkinkan untuk melakukan segmentasi pelanggan berdasarkan
      perilaku pembelian (RFM) serta mengidentifikasi pelanggan bernilai tinggi untuk strategi pemasaran yang tepat.
    </li>
  </ul>
  <p>Dataset ini sangat lengkap dan bisa digunakan untuk berbagai analisis yang mendalam, mulai dari perilaku pelanggan,
    performa produk, hingga efisiensi operasional. Langkah selanjutnya adalah <strong>assessing data</strong> untuk
    memahami kualitas data sebelum masuk ke analisis utama.</p>
</div>