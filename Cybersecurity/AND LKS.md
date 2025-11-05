# How to submit
```
curl -H 'Content-Type: application/json' -H 'Authorization: Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc1MzgzODQyNCwianRpIjoiM2FjNjJlOTEtYWE0ZC00NWQ5LWI3ZDgtN2U1ZTIyNzBmZThmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJ0ZWFtIjp7ImlkIjo3LCJuYW1lIjoiQmFsaSJ9fSwibmJmIjoxNzUzODM4NDI0LCJleHAiOjE3NTM4ODE2MjR9.jsGUAiivaqIU_tVHUcD6J4oNPvR7KK1L6aMZWKaWtQPM62abTNj3Db9b0_UHjfpLh0NgXoZX9NByDCA6sj2_EA' \
    -X POST --data '{"flags": ["LKSN{incorrect}", "LKSN{expired}", "LKSN{siwlzc8}", "LKSN{siwlzc8}"]}' \
    https://and-be.idcyberskills.com/api/v2/submit
```

```
<?php
$books = [
    ['id' => 'pendidikan-agama', 'title' => 'Pendidikan Agama dan Budi Pekerti', 'author' => 'Dr. KH. Abdullah Syukri', 'available' => true, 'category' => 'Wajib'],
    ['id' => 'pendidikan-pancasila', 'title' => 'Pendidikan Pancasila', 'author' => 'Prof. Dr. Sutrisno Pancasila', 'available' => true, 'category' => 'Wajib'],
    ['id' => 'buku-bahasa', 'title' => 'Bahasa Indonesia Komunikatif', 'author' => 'Drs. Bambang Wijaya', 'available' => false, 'category' => 'Wajib'],
    ['id' => 'penjas', 'title' => 'Pendidikan Jasmani, Olahraga, dan Kesehatan', 'author' => 'Dr. Fitria Sari Olahraga, M.Pd', 'available' => false, 'category' => 'Wajib'],
    ['id' => 'buku-sejarah', 'title' => 'Sejarah Indonesia Modern', 'author' => 'Dr. Ahmad Mansur', 'available' => true, 'category' => 'Wajib'],
    ['id' => 'seni-budaya', 'title' => 'Seni Budaya', 'author' => 'I Gede Seni Budaya, S.Sn., M.A', 'available' => true, 'category' => 'Wajib'],
    ['id' => 'buku-matematika', 'title' => 'Matematika Dasar SMK', 'author' => 'Prof. Siti Nurhaliza', 'available' => true, 'category' => 'Wajib'],
    ['id' => 'bahasa-inggris', 'title' => 'Bahasa Inggris', 'author' => 'Dr. Sarah Johnson & Drs. Budi English', 'available' => true, 'category' => 'Wajib'],
    ['id' => 'informatika', 'title' => 'Informatika', 'author' => 'Dr. Teknologi Digital, M.Kom', 'available' => false, 'category' => 'Wajib'],

    ['id' => 'buku-fisika', 'title' => 'Fisika Terapan', 'author' => 'Dr. Indira Sari', 'available' => true, 'category' => 'Kejuruan'],
    ['id' => 'buku-kimia', 'title' => 'Kimia Organik Praktis', 'author' => 'Prof. Hartono', 'available' => true, 'category' => 'Kejuruan'],
    ['id' => 'buku-ekonomi', 'title' => 'Ekonomi Bisnis Modern', 'author' => 'Dra. Wulan Dari', 'available' => false, 'category' => 'Kejuruan']
];
?>

<?php include 'partials/header.php'; ?>
<?php include 'partials/nav.php'; ?>

<main class="container mx-auto px-4 py-8">
    <!-- Hero Section -->
    <div class="bg-gradient-to-r from-blue-600 to-blue-800 text-white rounded-lg p-8 mb-8 text-center">
        <h1 class="text-4xl font-bold mb-4">Perpustakaan SMK 1 Indonesia Hebat</h1>
        <p class="text-xl opacity-90">Jendela Pengetahuan untuk Masa Depan Gemilang</p>
    </div>

    <!-- Available Books Section -->
    <section class="mb-12">
        <h2 class="text-3xl font-bold text-gray-800 mb-8 text-center">Koleksi Buku Kurikulum SMK</h2>

        <?php
        $categories = [];
        foreach ($books as $book) {
            $categories[$book['category']][] = $book;
        }
        ?>

        <?php foreach ($categories as $categoryName => $categoryBooks): ?>
            <div class="mb-10">
                <h3 class="text-2xl font-bold text-gray-700 mb-6 flex items-center">
                    <?php if ($categoryName === 'Wajib'): ?>
                        <i class="fas fa-star text-yellow-500 mr-3"></i>
                        Mata Pelajaran Wajib
                    <?php else: ?>
                        <i class="fas fa-cogs text-blue-500 mr-3"></i>
                        Mata Pelajaran Kejuruan
                    <?php endif; ?>
                    <span class="ml-2 text-sm font-normal text-gray-500">(<?php echo count($categoryBooks); ?> buku)</span>
                </h3>

                <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
                    <?php foreach ($categoryBooks as $book): ?>
                        <div class="bg-white rounded-lg shadow-lg p-6 border border-gray-200 hover:shadow-xl transition-shadow duration-300">
                            <div class="flex items-start justify-between mb-4">
                                <div class="flex-1">
                                    <div class="flex items-center mb-2">
                                        <?php if ($categoryName === 'Wajib'): ?>
                                            <span class="bg-yellow-100 text-yellow-800 text-xs font-medium px-2 py-1 rounded mr-2">WAJIB</span>
                                        <?php else: ?>
                                            <span class="bg-blue-100 text-blue-800 text-xs font-medium px-2 py-1 rounded mr-2">KEJURUAN</span>
                                        <?php endif; ?>
                                        <?php if ($book['available']): ?>
                                            <span class="bg-green-100 text-green-800 text-xs font-medium px-2 py-1 rounded">Tersedia</span>
                                        <?php else: ?>
                                            <span class="bg-red-100 text-red-800 text-xs font-medium px-2 py-1 rounded">Dipinjam</span>
                                        <?php endif; ?>
                                    </div>
                                    <h4 class="text-lg font-semibold text-gray-800 mb-2"><?php echo htmlspecialchars($book['title']); ?></h4>
                                    <p class="text-gray-600 mb-1 text-sm">Penulis: <?php echo htmlspecialchars($book['author']); ?></p>
                                </div>
                            </div>

                            <div class="flex gap-2">
                                <a href="/books/?name=<?php echo $book['id']; ?>.php" 
                                   class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded text-sm font-medium transition-colors duration-200 flex-1 text-center">
                                    Lihat Detail
                                </a>
                                <?php if ($book['available']): ?>
                                    <button class="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded text-sm font-medium transition-colors duration-200">
                                        Pinjam
                                    </button>
                                <?php endif; ?>
                            </div>
                        </div>
                    <?php endforeach; ?>
                </div>
            </div>
        <?php endforeach; ?>
    </section>

    <!-- Library Info -->
    <section class="bg-gray-50 rounded-lg p-8 text-center">
        <h3 class="text-2xl font-bold text-gray-800 mb-6">Informasi Perpustakaan</h3>
        <div class="grid md:grid-cols-4 gap-6">
            <div>
                <div class="text-3xl font-bold text-blue-600"><?php echo count($books); ?></div>
                <p class="text-gray-600">Koleksi Digital</p>
            </div>
            <div>
                <div class="text-3xl font-bold text-yellow-600"><?php echo count($categories['Wajib']); ?></div>
                <p class="text-gray-600">Mata Pelajaran Wajib</p>
            </div>
            <div>
                <div class="text-3xl font-bold text-green-600">24/7</div>
                <p class="text-gray-600">Akses Online</p>
            </div>
            <div>
                <div class="text-3xl font-bold text-purple-600">1500+</div>
                <p class="text-gray-600">Anggota Aktif</p>
            </div>
        </div>

        <div class="mt-8 p-4 bg-blue-50 rounded-lg">
            <p class="text-sm text-blue-800">
                <i class="fas fa-info-circle mr-2"></i>
                Perpustakaan digital dengan koleksi lengkap kurikulum SMK sesuai standar Kemendikbud
            </p>
        </div>
    </section>
</main>

<?php include 'partials/footer.php'; ?>                                            
```

LKSN{owp27zobl6v8ju2fh6spnfrn}
LKSN{vqrtmsmg24294esp4a3f74qb}
LKSN{ni3szlrxhpcsngdhmtajiuju}
LKSN{vays1tfww9vzdxccwa8io9c8
